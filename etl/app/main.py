import uvicorn
import psycopg2
import numpy as np

from fastapi import FastAPI

from app.db import bulk_insert
from app.models import EtlRequest, Shift, KPI
from app.calculations import get_kpi_statistic

app = FastAPI(title="Etl Job API")


@app.post(
    "/api/perform_job",
    summary="Perform Etl Job",
    description="Returns paginated shifts response. Each response contains "
    "navigation links with 'prev' and 'next' fields. When response does not contain "
    "'prev' field, then results correspond to the first page. When response does not "
    "contain 'next' field, than there are no more results.",
)
def perform_job(request: EtlRequest):

    shifts = request.results
    conn = None

    try:
        conn = psycopg2.connect(
            host="postgres",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        cur = conn.cursor()

        for shift in shifts:
            shift.cost = np.sum(list(map(lambda allowance: allowance.cost, shift.allowances))) + np.sum(
                list(map(lambda award: award.cost, shift.award_interpretations)))

            for bulk in [bulk_insert('shifts', [shift]), bulk_insert('breaks', shift.breaks, shift),
                         bulk_insert('allowances', shift.allowances, shift), bulk_insert('award_interpretations', shift.award_interpretations, shift)]:
                if bulk:
                    cur.execute(bulk)

        cur.execute(bulk_insert('kpis', get_kpi_statistic(shifts)))
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit()
            conn.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

