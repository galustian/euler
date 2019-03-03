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

# top-down DP
def compute():
    sum_ = 1
    for vars_ in range(2, 100):
        sum_ += numWaysSum(100, vars_, 100)
    return sum_

#def print_array(array):
#    for i in range(len(array)):
#        print(array[i])

# bottom-up DP
def compute2():
    ways = [[0]*101 for i in range(101)]
    ways[0] = [0] + [1] * 100

    for sum_ in range(1, 101):
        for upper in range(1, 101):
            if upper > sum_:
                ways[sum_][upper] = ways[sum_][sum_]
                continue
            
            ways[sum_][upper] = ways[sum_][upper-1] + ways[sum_-upper][upper]

    return ways[100][100] - 1

if __name__ == '__main__':
    print(compute())
    print(compute2())
