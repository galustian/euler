from util import is_prime
import time

# test with and without global primes
prime_table = None

def prime_factors(n):
    factors = []
    for p in prime_table:
        if n % p != 0: continue
        factors.append(p)
        while n % p == 0: n //= p
    
    return factors

def eulers_phi(n):
    for p in prime_factors(n): n *= 1 - 1/p
    return n

def compute():
    largest_ratio = 1
    num = 1
    
    for i in range(1000, 1_000_000, 2):
        ratio = i / eulers_phi(i)
        if ratio > largest_ratio:
            largest_ratio = ratio
            num = i
    
    return num, largest_ratio

def compute2():
    return 2 * 3 * 5 * 7 * 11 * 13 * 17 # * 19 would be > 1_000_000

if __name__ == '__main__':
    prime_table = [2] + [i for i in range(3, 998, 2) if is_prime(i)]
    
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
