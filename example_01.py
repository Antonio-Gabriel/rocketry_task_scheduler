"""
    Example 01 - Rocketry
    Case: here we also can find the possibility to specify 
    the periode that the task will run

    Connectives: 
    [ every, 1, 'second' ], [ every, 10, 'seconds' ],
    [ every, 1, 'day' ], [ every, 2, 'days' ],

    Representation: every <TIME> connective

    Other connectives are:
     - millisecond -> ms
     - second -> {
        - seconds
        - sec
        - s
     }     
     - minute -> {
        - minutes
        - mins
        - min
        - m
     }
     - hour -> {
        - hours
        - h
     }
     - day -> {
        - days
        - d
     }
"""

from random import choice

from rocketry import Rocketry
from rocketry.conds import minutely, every

scheduler = Rocketry(execution='async')

@scheduler.task('every 1 second')
async def every_one_second():
    """to each one second tell a random greet again"""
    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    print(choice(greet_list), "second")


@scheduler.task(every('1d'))
async def every_one_day():
    """to each one day tell a random greet again"""
    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    print(choice(greet_list), "day")


"""other way to specify the minutely of task as object no string"""
@scheduler.task(minutely)
async def greeting():    
    """to each minute tell a random greet"""

    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    print(choice(greet_list))

scheduler.run()
