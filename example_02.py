"""
    Example 02 - Rocketry
    Case: restricts

    Connectives: 
    [ every, 1, 'second' ], [ every, 10, 'seconds' ],
    [ every, 1, 'day' ], [ every, 2, 'days' ],

    Representation: period <cond> : {
        between : <s_time><e_time>,
        before, after : <time>         
    }
"""

from random import choice

from rocketry import Rocketry
from rocketry.conds import hourly

scheduler = Rocketry(execution='async')

@scheduler.task('minutely after 10sec')
async def greeting():    
    """to each minute tell a random greet"""

    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    print(choice(greet_list), 'minute')

@scheduler.task(hourly.after('10:20'))
async def greeting_per_hour():    
    """to each hour tell a random greet"""

    greet_list = [
        'Hello', 'Good Morning', 
        'Good Evening', 'Good bye'
        ]
    print(choice(greet_list), 'hour')

scheduler.run()
