"""
    Example 00: other tips - Rocketry
    A Point: we can run the tasks on differents time such as 
    `minutely`, `hourly`, `daily`, `weekly`, `monthly`
"""

from random import choice
from rocketry import Rocketry

scheduler = Rocketry(execution='async')

@scheduler.task('minutely')
async def greeting_per_minute():
    """to each minute tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list), " minute")

@scheduler.task('hourly')
async def greeting_per_hour():
    """to each hourly tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list), " hourly")

@scheduler.task('daily')
async def greeting_per_day():
    """to each daily tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list), " daily")

@scheduler.task('weekly')
async def greeting_per_week():
    """to each weekly tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list), " weekly")

@scheduler.task('monthly')
async def greeting_per_month():
    """to each monthly tell a random greet"""

    greet_list = ['Hello', 'Good Morning', 'Good Evening', 'Good bye']
    print(choice(greet_list), " monthly")

scheduler.run()
