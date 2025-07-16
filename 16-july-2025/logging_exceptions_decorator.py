import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

"""A Function to execute add and subtract functions"""
def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

func1 = logger(add)
func2 = logger(subtract)
func1(3,5)
func2(5,0)
