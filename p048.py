def modular_exp(a, exp=1, mod=1):
    if exp <= 5:
        return (a**exp) % mod
    return (modular_exp(a, exp=exp//2, mod=mod) * modular_exp(a, exp=exp - exp//2, mod=mod)) % mod

def compute():
    sum_ = 0
    mod = 10**10
    for i in range(1, 1001):
        sum_ += modular_exp(i, i, mod)
    return sum_ % mod

if __name__ == '__main__':
    print(compute())
