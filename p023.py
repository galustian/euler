import time
from util import gen_prime_table, is_prime

prime_table = None

def prime_factorization(n):
    if is_prime(n): return {n: 1}

    prime_factors = {}

    for p in prime_table:
        if p > n: break
        while n % p == 0:
            n /= p
            prime_factors[p] = prime_factors.get(p, 0) + 1

    return prime_factors

def sum_of_divisors(n):
    prime_factors = prime_factorization(n)
    sum_of_divisors = 1
    for prime, times in prime_factors.items():
        sum_of_divisors *= (prime**(times+1) - 1) // (prime - 1)
    return sum_of_divisors - n

#https://en.wikipedia.org/wiki/Abundant_number
def compute():
    # compute all abundant numbers from 12 to 28111 START
    abuntant_set = set()
    abuntant_list = []

    for i in range(12, 28112):
        if i in abuntant_set: continue
        if i % 6 == 0 or sum_of_divisors(i) > i:
            j = 1
            while i * j <= 28111:
                i_mult = i * j
                if i_mult in abuntant_set:
                    j += 1
                    continue
                abuntant_set.add(i_mult)
                abuntant_list.append(i_mult)
                j += 1
    
    abuntant_list.sort()
    # compute all abundant numbers from 12 to 28111 END
    
    not_two_abuntants_sum = (23 + 1)*23//2

    for i in range(24, 28123):
        not_sum = True
        for ab in abuntant_list:
            if i - ab < 12: break
            if i - ab in abuntant_set:
                not_sum = False
                break
        
        if not_sum: not_two_abuntants_sum += i
    
    return not_two_abuntants_sum


if __name__ == '__main__':
    start = time.time()
    prime_table = gen_prime_table(19957)
    print(compute())
    print(time.time() - start)