import time
def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Calling function `{cache_dict}`")
        if args in cache_dict:
            # print(f"Cache hit for arguments: {args}")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Function `{func.__name__}` with arguments {args} took {elapsed_time:.4f} seconds to retrieve from cache.")
            return cache_dict[args]
        
        result = func(*args, **kwargs)
        cache_dict[args] = result
        # print(f"Cache miss for arguments: {args}. Result cached.")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function `{func.__name__}` with arguments {args} took {elapsed_time:.4f} seconds to retrieve from cache.")
        return result
    
    return wrapper

@cache
def long_time_function(x, y):
    time.sleep(4)
    return x + y



print(f'Result 01: {long_time_function(1,3)}')
print(f'Result 02: {long_time_function(1,3)}')
print(f'Result 03: {long_time_function(1,3)}')
print(f'Result 04: {long_time_function(5,3)}')