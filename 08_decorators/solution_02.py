import time

def debug(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        arg_str = ', '.join(str(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        result = func(*args, **kwargs)
        end= time.time()
        elapsed_time = end - start_time
        print(f"Calling function `{func.__name__}` with arguments: {arg_str} and kwargs: {kwargs_str} took {elapsed_time:.4f} seconds.")
        return result
    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


@debug
def hello():
    time.sleep(3)
    print("hello word")

hello()
greet("Atik", greeting="Hi")