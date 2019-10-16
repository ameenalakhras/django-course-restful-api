from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab


# from restProject.celery import app

from celery.decorators import task

# whenever this function is called, it does its functionalities
# with syncronyzation to the user browsing ability
@task(name="sum_two_numbers")
def add(x, y):
    import time
    time.sleep(5)
    return x + y
# you call this function by # add.delay(7, 8)
# you MUST add "delay"


logger = get_task_logger(__name__)


# execute every two minutes
# YOU MUST run both selery workers and selery beat
# (at the time of running the project)
@periodic_task(
    run_every=(crontab(minute='*/2')),
    name="some_task",
    ignore_result=True
)
def some_task():
    print("doing something is working")
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return ("Current Time =", current_time)
