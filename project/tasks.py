from project.celery_app import app
from celery import group

from project.parser import RequestParser, get_urls_to_parse


@app.task
def schedule_request(url: str):
    result = RequestParser.parse(url=url)
    return result


@app.task
def schedule_requests():
    urls = get_urls_to_parse()
    group((schedule_request.si(url) for url in urls)).apply_async()
