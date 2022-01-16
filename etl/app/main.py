import uvicorn
import numpy as np

from fastapi import FastAPI
from sqlalchemy import create_engine

from app.db import bulk_insert
from app.models import EtlRequest, Shift, KPI
from app.calculations import get_kpi_statistic

app = FastAPI(title="Etl Job API")
db_engine = create_engine('postgresql://postgres:postgres@postgres:5432/postgres')


@app.post(
    "/api/perform_job",
    summary="Perform Etl Job",
    description="Consumes data from endpoint, performs KPI transformations  "
                "and stores results into database.",
    status_code=201
)
def perform_job(request: EtlRequest) -> None:

    shifts = request.results

    with db_engine.connect() as conn:
        for shift in shifts:
            shift.cost = np.sum(list(map(lambda allowance: allowance.cost, shift.allowances))) + np.sum(
                list(map(lambda award: award.cost, shift.award_interpretations)))

            for bulk in [bulk_insert('shifts', [shift]), bulk_insert('breaks', shift.breaks, shift),
                         bulk_insert('allowances', shift.allowances, shift), bulk_insert('award_interpretations', shift.award_interpretations, shift)]:
                if bulk:
                    conn.execute(bulk)

        conn.execute(bulk_insert('kpis', get_kpi_statistic(shifts)))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

