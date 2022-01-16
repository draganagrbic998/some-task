# Shifts ETL

Work shifts for the past year are exposed through paginated REST API. Your
task is to consume data from endpoint, perform specified transformations and
store results into specified database (i.e. create an ETL job).

All ETL job related code should be inside [etl](./etl) dir. Make sure to
write clear instructions how to setup and run ETL job.

<p align="center">
    <img src="./diagram.png">
</p>

## Getting Started

Besides chosen language and tools for ETL job, you will need `docker` and `docker-compose`.

Initialize & start shifts API and target Postgres database in the background
with

```bash
$ docker-compose up -d
```

### Shift API

Shift API spec is available at [Shift API Spec](http://localhost:8000/redoc).
Endpoints return randomly generated (with fixed seed for reproducibility)
shifts data for the previous year. There is not authentication mechanism.

### Postgres

Transformed shifts data should be saved to the Postgres instance running at
`localhost:5432` inside default `postgres` database. Default username and
password are `postgres:postgres`. The database is already initialized with
output tables:

- `shifts`
- `breaks`
- `allowances`
- `award_interpretations`
- `kpis`

Check out [db initialization script](./initdb.sql) for more details.

### pgAdmin

An instance of pgAdmin is running at
[http://localhost:5050](http://localhost:5050) configured with following
login information:

- username: `pgadmin@smartcat.io`
- password: `pgadmin`

After you log in, add a new database server. Postgres server is available
under `postgres` hostname because `pgAdmin` and `postgres` servers are inside
same docker network.

## Tasks

ETL job should perform transformations specified bellow. Consider scenarios
when job might fail.

### 1. Extract Models

Raw shift data contain nested models: breaks, allowances and award
interpretations. Extract these records and insert them into corresponding
Postgres tables: `shifts`, `breaks`, `allowances`, and `award_interpretations`.

Additional requirements:

- All IDs should be preserved (generated UUIDs)
- All records returned from the shifts API must be saved into database
- Calculate total shift cost (`shift.cost` field) that is equal to the sum of
all costs inside one shift (allowance costs + award interpretation costs)

### 2. Calculate Shift KPIs

Use extracted shifts data to calculate defined KPIs. KPIs are uniquely
identified by KPI name and date when KPIs are calculated.

| Name                                  	| Description                                                            	|
|---------------------------------------	|------------------------------------------------------------------------	|
| `mean_break_length_in_minutes`        	| Mean shift break time in minutes (`breaks.start` and `breaks.finish`). 	|
| `mean_shift_cost`                     	| Mean shift cost (`shifts.cost`).                                       	|
| `max_allowance_cost_14d`              	| Max allowance cost in the last 14 days (`allowances.cost`).            	|
| `max_break_free_shift_period_in_days` 	| Longest period in days when consecutive shifts did not have breaks.    	|
| `min_shift_length_in_hours`              	| Shortest shift duration (`shift.start` and `shift.finish`).            	|
| `total_number_of_paid_breaks`         	| Total number of paid shift breaks (`breaks.is_paid`).                  	|

## Deliverables

- Working or even non-working code sent in zip archive or shared via git repository
- Code should be written in Java or Python
- Code should contain README file that explains the approach and how to run the applications
- Deployment and cleanup should be as simple as possible

## General Advice

- Use common sense
- Keep things simple
- It’s much better to have a working solution than the perfect, but not working solution

## Evaluation Criteria

The top is the most important:

- Finished working sample (usable ETL job with clear instructions how to run and use)
- Code quality (idiomatic Python or Java)
- Design quality (proper abstractions)
- Tests
- Performance
- Documented code (when it’s relevant)

Remember that simple is better than complex, and complex is better than
complicated.

Good luck & have fun!

## ETL Job Task

<p style="text-align: justify">
The ETL Job is implemented using Python and FastAPI. All related code is placed inside [etl](./etl) dir. Directory contains **app** package which holds the main logic and another **test** package used for unit testing. App package consists of four files - **model.py**, **db.py**, **calculations.py** and **main.py**. Every file holds appropriate comments/documentation, if you want to get more details. 
</p>

Since ETL Job is implemented as another docker service, running and usage is pretty simple. I updated docker-compose.yml file with necessary changes that were needed for its deployment (check the file for more details). Accordingly, you can run the whole application (postgres, pgadmin, shifts-api and etl-job) only by clonning this repo, positioning in the root dir and running `docker-compose up -d` command. The ETL Job listens on 8001 port, you can check its REST api on [http://localhost:8001/docs](http://localhost:8001/docs) and [http://localhost:8001/redoc](http://localhost:8001/redoc). 

The test package inside [etl](./etl) dir holds two files - **data.py** and **test.py**. The first one holds data used when testing, the second one testing logic itself. Unit tests are used for verifying that methods used for KPI statistic calculation work as they should. To run those tests locally first you have to install python packages inside your virtual environvement with the command `pip install -r requirements.txt` (where requirements.txt file holds all dependency modules needed for application to start, file is placed in the root directory). The next step is to position in the [etl](./etl) directory and run command `python -m test.test`. If everything goes right, you should see that 5 tests have passed successfully.


