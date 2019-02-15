from math import factorial

def n_choose_c(n, c): return factorial(n) // (factorial(n - c) * factorial(c))

def compute():
    greater_than_million = 0

    for n in range(10, 101):
        if n % 2 == 0 and n_choose_c(n, n // 2) > 1_000_000: greater_than_million += 1
        for c in range(3, n//2 + 1):
            if c == n//2 and n % 2 == 0: continue
            if n_choose_c(n, c) > 1_000_000: greater_than_million += 2
    
    return greater_than_million

if __name__ == '__main__':
    print(compute())
