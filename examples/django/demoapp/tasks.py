from __future__ import absolute_import

from celery import shared_task, Task
from celery.utils.log import get_task_logger

#@shared_task
#def add(x, y):
#    return x + y
@shared_task
class AddTask(Task):
 
    @property
    def log(self):
        return get_task_logger('%s.%s' % (__name__, self.__class__.__name__))
 
    def run(self, x, y):
        self.log.info("Calling task add(%d, %d)" % (x, y))
        return x + y

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
