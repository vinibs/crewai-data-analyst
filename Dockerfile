FROM python:3.12-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    default-libmysqlclient-dev

COPY requirements/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src .

CMD ["python", "main.py"]