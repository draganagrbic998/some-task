FROM python:3.7-slim

WORKDIR /etl

COPY requirements.txt /etl/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /etl/requirements.txt

COPY app /etl/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
