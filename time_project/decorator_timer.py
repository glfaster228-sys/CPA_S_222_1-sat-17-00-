import time
import functools


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        execution_time = end - start
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.6f} секунд")

        return result

    return wrapper