"""
    Example 04 - Rocketry
    Case: I can get the return of a process in other process
"""

import logging
from random import choice

from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import (
    after_success, after_all_finish
    )

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

scheduler = Rocketry(execution='async')

@scheduler.task('every 2 seconds')
async def greet_process():
    """select a random greet"""
    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    
    return choice(greet_list)

@scheduler.task(after_success(greet_process))
def greet_process_done(value=Return(greet_process)):
    """run when task process is done"""
    print("greet_process value is: ", value)

@scheduler.task(after_all_finish(greet_process, greet_process_done))
def task_process_finish():
    """run when task process is done"""
    print("the task is finished")

scheduler.run()
