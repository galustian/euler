from math import sqrt
from util import is_prime

def compute():
    prime_table = [2, 3]
    def primes_below(n):
        for i in range(prime_table[-1]+2, n, 2):
            if is_prime(i): prime_table.append(i)
        return prime_table

    composite = 5
    while True:
        if is_prime(composite):
            composite += 2
            continue

        goldbach_is_wrong = True
        for p in primes_below(composite):
            if sqrt((composite - p) // 2).is_integer():
                goldbach_is_wrong = False
                break
        
        if goldbach_is_wrong: return composite
        
        composite += 2

    return composite

if __name__ == '__main__':
    print(compute())