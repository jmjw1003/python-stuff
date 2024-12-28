import time
import logging
from functools import wraps, update_wrapper

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

"""
A few example implementations of decorators
"""

def timer(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer


def debug(func):
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug


def log(func):
    @wraps(func)
    def wrapper_log(*args, **kwargs):
        try:
            logger.debug(f"Running {func.__name__}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. Exception: {str(e)}")
            raise e
    return wrapper_log

"""
Decorators with arguments
"""

def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


def log_with_level(level, logger=logger):
    def decorator_log_with_level(func):
        @wraps(func)
        def wrapper_log_with_level(*args, **kwargs):
            logger.log(level, f"Running {func.__name__}")
            return func(*args, **kwargs)
        return wrapper_log_with_level
    return decorator_log_with_level


"""
Class decorators
"""

class CountCalls:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return value


"""
Code to test the decorators
"""

@log
def foo():
    print("Hello from foo")
    raise Exception("Something went wrong")

@repeat(3)
def bar():
    print("Hello from bar")

@timer
def baz():
    print("Hello from baz")
    time.sleep(3)

@CountCalls
def boo():
    print("Hello from boo")

if __name__ == "__main__":
    for _ in range(3):
        boo()
