from math import sqrt

def is_pent(x): return (1 + sqrt(24*x + 1)) % 6 == 0

# insight: hexagonal numbers are a subset of triangular numbers
def compute():
    n = 144
    while True:
        hx = n*(2*n - 1)
        if is_pent(hx): return hx
        n += 1

if __name__ == '__main__':
    print(compute())