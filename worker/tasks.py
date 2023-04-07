from time import sleep
from worker import celery

@celery.task(bind=True)
def logging(self):
    sleep(10)
    print(self.name)