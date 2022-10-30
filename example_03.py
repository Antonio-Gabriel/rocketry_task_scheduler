"""
    Example 03 - Rocketry
    Case: piplines and triggers
"""

import logging
from random import randint

from rocketry import Rocketry
from rocketry.conds import (
    after_success, after_all_finish
    )

# The rocketry already have your logger structure configured, and we can
# see the occurred error at terminal.
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

scheduler = Rocketry(execution='async')

@scheduler.task('every 2 seconds')
async def task_process():
    """select a number range 0 and 1"""
    
    if randint(0, 1):
        raise Exception('An error occured')
    
    print("success")

@scheduler.task(after_success(task_process))
def task_process_done():
    """run when task process is done"""
    print("the task is done")

@scheduler.task(after_all_finish(task_process, task_process_done))
def task_process_finish():
    """run when task process is done"""
    print("the task is finished")


scheduler.run()
