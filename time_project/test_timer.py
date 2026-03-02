import time
from timer import measure_time
from decorator_timer import timing_decorator


def test_measure_time_returns_correct_result():
    def test_func():
        return 100

    result, exec_time = measure_time(test_func)

    assert result == 100
    assert exec_time >= 0


def test_measure_time_with_sleep():
    def slow_func():
        time.sleep(0.3)
        return "done"

    result, exec_time = measure_time(slow_func)

    assert result == "done"
    assert exec_time >= 0.3


def test_timing_decorator_returns_correct_value():
    @timing_decorator
    def test_func():
        time.sleep(0.2)
        return 5

    result = test_func()

    assert result == 5