from functools import lru_cache
from math import sqrt, floor

def is_pen(x):
    return (1 + sqrt(24*x + 1)) % 6 == 0

@lru_cache(maxsize=None)
def pen(n):
    return n*(3*n - 1) // 2

def compute():
    min_pentagon_diff = None
    
    j = 7
    while True:
        pen_j = pen(j)
        pen_jp1 = pen(j+1)

        for k in reversed(range(j)):
            if pen_j + pen(k) < pen_jp1: break
            
            if is_pen(pen_j + pen(k)) and is_pen(pen_j - pen(k)):
                min_pentagon_diff = pen_j - pen(k)
                print(min_pentagon_diff)
        
        j += 1


if __name__ == '__main__':
    print(compute())