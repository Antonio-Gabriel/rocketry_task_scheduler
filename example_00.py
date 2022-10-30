"""
    Example 00 - Rocketry
    Case: runs the task to each minute
"""

from random import choice
from rocketry import Rocketry

scheduler = Rocketry(execution='async')

@scheduler.task('minutely')
async def greeting():
    """to each minute tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list))

scheduler.run()
