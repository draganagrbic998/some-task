from fastapi import FastAPI
import uvicorn
import psycopg2
import numpy as np

from datetime import datetime

from app.models import EtlRequest
from app.calculations import calculate_mean_break_length_in_minutes, calculate_mean_shift_cost, \
    calculate_max_allowance_cost_14d, calculate_min_shift_length_in_hours, calculate_total_number_of_paid_breaks

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
            password="postgres")
        cur = conn.cursor()

        start_date = None
        end_date = None
        max_break_free_shift_period_in_days = 0

        for shift in sorted(shifts, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d')):
            shift.cost = np.sum(list(map(lambda allowance: allowance.cost, shift.allowances))) + np.sum(list(map(lambda award: award.cost, shift.award_interpretations)))

            shift_row = "('%s', '%s', to_timestamp(%s), to_timestamp(%s), %s)" % (shift.id, shift.date, shift.start, shift.finish, shift.cost)
            break_rows = ','.join("('%s','%s',to_timestamp(%s),to_timestamp(%s),%s)" % (br.id, shift.id, br.start, br.finish, 'true' if br.paid else 'false') for br in shift.breaks)
            allowance_rows = ','.join("('%s','%s',%s,%s)" % (allowance.id, shift.id, allowance.value, allowance.cost) for allowance in shift.allowances)
            award_rows = ','.join("('%s','%s','%s',%s,%s)" % (award.id, shift.id, award.date, award.units, award.cost) for award in shift.award_interpretations)

            cur.execute("insert into shifts values " + shift_row + " on conflict do nothing")
            if break_rows:
                cur.execute("insert into breaks values " + break_rows + " on conflict do nothing")
            if allowance_rows:
                cur.execute("insert into allowances values " + allowance_rows + " on conflict do nothing")
            if award_rows:
                cur.execute("insert into award_interpretations values " + award_rows + " on conflict do nothing")

            if len(shift.breaks) <= 0:
                start_date = None
            if len(shift.breaks) > 0 and not start_date:
                start_date = shift.date

            end_date = shift.date

        if start_date and end_date:
            max_break_free_shift_period_in_days = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days


        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('mean_break_length_in_minutes', calculate_mean_break_length_in_minutes(shifts)))
        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('mean_shift_cost', calculate_mean_shift_cost(shifts)))
        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('max_allowance_cost_14d', calculate_max_allowance_cost_14d(shifts)))
        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('max_break_free_shift_period_in_days', max_break_free_shift_period_in_days))
        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('min_shift_length_in_hours', calculate_min_shift_length_in_hours(shifts)))
        cur.execute("insert into kpis (kpi_name, kpi_date, kpi_value) values ('%s', current_date, %s)" % ('total_number_of_paid_breaks', calculate_total_number_of_paid_breaks(shifts)))

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        import traceback
        print(error)
        print(traceback.format_exc())
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

