
from celery import Celery

celery = Celery("multiple_worker", broker="amqp://guest:guest@localhost:5672")

from worker import tasks