from math import floor

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def compute():
    n_prod, d_prod = 1, 1

    for i in range(1, 10):
        for d in range(1, 10):
            for n in range(1, min(i, d)):
                if n / d == (10*n + i) / (10*i + d):
                    d_prod *= d
                    n_prod *= n
    
    return d_prod / gcd(d_prod, n_prod)

if __name__ == '__main__':
    print(compute())