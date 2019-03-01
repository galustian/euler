from math import factorial
from functools import lru_cache

@lru_cache(maxsize=None)
def numWaysSum(sum_, vars_, upper_):
    if vars_ == 1: return 1
    ways = 0
    for n in reversed(range(1, upper_+1)):
        if n * (vars_-1) < sum_-n: break
        if sum_-n < vars_-1: continue
        ways += numWaysSum(sum_-n, vars_-1, n)
    return ways

def compute():
    sum_ = 1
    for vars_ in range(2, 100):
        sum_ += numWaysSum(100, vars_, 100)
    return sum_

if __name__ == '__main__':
    print(compute())
