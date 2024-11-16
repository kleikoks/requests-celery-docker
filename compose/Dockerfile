FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

COPY ./compose/start-project /start-project
RUN sed -i 's/\r$//g' /start-project
RUN chmod +x /start-project

COPY ./compose/start-celery-worker /start-celery-worker
RUN sed -i 's/\r$//g' /start-celery-worker
RUN chmod +x /start-celery-worker

COPY ./compose/start-celery-flower /start-celery-flower
RUN sed -i 's/\r$//g' /start-celery-flower
RUN chmod +x /start-celery-flower

RUN python -m pip install --upgrade --no-cache-dir pip

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

