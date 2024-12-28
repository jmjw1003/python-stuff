import time
import logging
from functools import wraps

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
Code to test the decorators
"""

@log
def foo():
    print("Hello from foo")
    raise Exception("Something went wrong")

if __name__ == "__main__":
    foo()
