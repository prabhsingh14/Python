import time

def cache(func):
    cache_val = {}
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result = func(*args)
        cache_val[args] = result
        return result
    return wrapper

@cache
def long_running_function():
    time.sleep(4)
    return "NASA HACKED"

print(long_running_function())