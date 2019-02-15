import time
from util import gen_prime_table, is_prime

def compute():
    primes = gen_prime_table(1000)
    primes_set = set(primes)
    
    def num_prime_factors(n):
        num_factors = 0
        for p in primes:
            if p > n: return num_factors
            if n % p == 0: num_factors += 1
            while n % p == 0: n //= p

    num = 330
    while True:
        num0 = num_prime_factors(num) == 4
        num1 = num_prime_factors(num+1) == 4
        num2 = num_prime_factors(num+2) == 4
        num3 = num_prime_factors(num+3) == 4
        
        if num0 and num1 and num2 and num3: return num
        
        if num2 and num3: num += 2
        elif num3: num += 3
        else: num += 1
    


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)