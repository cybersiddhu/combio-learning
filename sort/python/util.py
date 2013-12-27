"""Utility functions """


def fib_iterative(num):
    """Generate fibonacci series using iteration"""
    series = [0, 1]
    for i in range(2, num + 1):
        series.append(series[i - 1] + series[i - 2])
    return tuple(series)


def fib_recursive(num):
    """Generate fibonacci series using recursion"""
    series = []
    for i in range(0, num + 1):
        series.append(fibnr(i))
    return tuple(series)


def fibnr(num):
    """Generate fibonacci number using recursion"""
    if num < 2:
        return num
    return fibnr(num - 1) + fibnr(num - 2)
