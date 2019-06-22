# having *params in the paramaters allows for mutliple parameter,
# it also lets it pass the parameters to the function that is being called
# from colors import bcolors


def rep_func(func, times, *params):
    for x in range(times):
        func(*params)
