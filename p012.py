import math
from util import next_largest_prime, gen_prime_table

prime_table = []

def prime_factorization(n):
    global prime_table
    prime_factors = {}
    
    for prime in prime_table:        
        if prime > n: break

        while n % prime == 0:
            n /= prime
            if prime in prime_factors:
                prime_factors[prime] += 1
            else:
                prime_factors[prime] = 1
        
    return prime_factors

# https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html
def number_of_divisors(n):
    prime_factors = prime_factorization(n)

    product = 1
    for prime in prime_factors:
        product *= prime_factors[prime] + 1

    return product


def first_number_with_n_divisors(n):
    prime_factors = {}

    for number in range(2, n+1):
        pr_factors = prime_factorization(number)
        for prime in pr_factors:
            if prime in prime_factors and prime_factors[prime] < pr_factors[prime]:
                prime_factors[prime] += pr_factors[prime] - prime_factors[prime]
            else:
                prime_factors[prime] = pr_factors[prime]

        n_divisors = 1
        for prime in prime_factors:
            n_divisors *= prime_factors[prime] + 1
            
            if n_divisors >= n:
                product = 1
                for p in prime_factors:
                    product *= p ** prime_factors[p]
                return product
    
    print("Flawed Logic...")


def compute_with_lower_bound():    
    global prime_table
    
    prime_table = gen_prime_table(100)
    
    n = math.ceil(math.sqrt(first_number_with_n_divisors(501) + 1/4) - 1/2)

    n_divisors = number_of_divisors(n * (n + 1) / 2)
    
    while n_divisors < 501:
        n += 1
        if n % 2 == 0:
            n_divisors = number_of_divisors(n / 2) * number_of_divisors((n + 1))
        else:
            n_divisors = number_of_divisors((n + 1) / 2) * number_of_divisors(n)
    
    return int(n * (n + 1) / 2)


if __name__ == '__main__':
    import time
    start = time.time()
    print(compute_with_lower_bound())
    print(time.time() - start)