import sys
sys.setrecursionlimit(10000)


def fact(n):
    """function to calculate fact"""
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)


print(fact(10))
