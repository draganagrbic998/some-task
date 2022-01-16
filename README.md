## ETL Job Task

The ETL Job is implemented using Python and FastAPI. All related code is placed inside [etl](./etl) dir. Directory contains **app** package which holds the main logic and another **test** package used for unit testing. App package consists of four files - **model.py**, **db.py**, **calculations.py** and **main.py**. Every file holds appropriate comments/documentation, if you want to get more details. 

Since ETL Job is implemented as another docker service, running and usage is pretty simple. I updated docker-compose.yml file with necessary changes that were needed for its deployment (check the file for more details). Accordingly, you can run the whole application (postgres, pgadmin, shifts-api and etl-job) only by clonning this repo, positioning in the root dir and running `docker-compose up -d` command. The ETL Job listens on 8001 port, you can check its REST api on [http://localhost:8001/docs](http://localhost:8001/docs) and [http://localhost:8001/redoc](http://localhost:8001/redoc). 

The test package inside [etl](./etl) dir holds two files - **data.py** and **test.py**. The first one holds data used when testing, the second one testing logic itself. Unit tests are used for verifying that methods used for KPI statistic calculation work as they should. To run those tests locally first you have to install python packages inside your virtual environvement with the command `pip install -r requirements.txt` (where requirements.txt file holds all dependency modules needed for application to start, file is placed in the root directory). The next step is to position in the [etl](./etl) directory and run command `python -m test.test`. If everything goes right, you should see that 5 tests have passed successfully.


