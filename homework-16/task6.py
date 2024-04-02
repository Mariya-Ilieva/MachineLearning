import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = (end_time - start_time) * 1000

        print(f'{func.__name__}({args}, {kwargs}), executed in {elapsed_time:.2f} ms')

        return result

    return wrapper

@time_decorator
def sort_test(arr, repeat):
    for _ in range(repeat):
        b = sorted(arr)

sort_test([3, 5, 5, 8, 12], 11000)
