import click, colorama

from colorama import Fore, Back
from src import logger


@click.command()
@click.option('-name', default='Jimmy', help='says hello to user!')
@click.option('-count', default=1, help='The count of times it says hello')
def hello(name, count):
    for x in range(count):
        msg = f'{Fore.BLUE+Back.RED}Hello {name}! I have said hello to you {x+1} times!'
        print(msg)


if __name__ == '__main__':
    hello()
    # ddd = 'jksdfsdf'
    # logger.log("Testing log....")
    # logger.logtofile("Testing logtofile....", file="logs\\testlog.log")
