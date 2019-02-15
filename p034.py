import time
import math
from math import log10, floor

def digit_at_idx(digit, i):
    return floor(digit / 10**(i-1)) % 10

def compute():
    factorial = {i:math.factorial(i) for i in range(0, 10)}

    total = 0

    for num in range(11, 2_540_160):
        num_magnitude = floor(log10(num)) + 1
        digit_factorial_sum = 0
        for i in range(1, num_magnitude+1):
            digit_factorial_sum += factorial[floor(num / 10**(i-1)) % 10]

        if digit_factorial_sum == num:
            total += num
    
    return total

if __name__ == '__main__':
    start = time.time()
    print(compute())
    print(time.time() - start)