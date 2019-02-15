import time
from math import log10, floor
from util import is_prime

def compute1():
    # truncate left to right / right to left
    def all_primes(num_str):
        all_primes = True
        for i in range(1, len(num_str)):
            left_num, right_num = int(num_str[i:]), int(num_str[:-i])
            
            left_is_prime = left_num not in not_prime_set and (left_num in is_prime_set or is_prime(left_num))
            right_is_prime = right_num not in not_prime_set and (right_num in is_prime_set or is_prime(right_num))
            
            if left_is_prime: is_prime_set.add(left_num)
            if right_is_prime: is_prime_set.add(right_num)
            
            if not left_is_prime:
                all_primes = False
                not_prime_set.add(left_num)
                break
            if not right_is_prime:
                all_primes = False
                not_prime_set.add(right_num)
                break
       
        return all_primes

    num = 12
    primes = []
    is_prime_set, not_prime_set = set(), set()

    while len(primes) < 11:
        num_0, num_1 = num-1, num+1
        num_str_0, num_str_1 = str(num_0), str(num_1)
        
        is_truncatable_candidate_0 = num_0 not in not_prime_set and not ('0' in num_str_0 or '4' in num_str_0 or '6' in num_str_0 or '8' in num_str_0) and (num_0 in is_prime_set or is_prime(num_0))
        is_truncatable_candidate_1 = num_1 not in not_prime_set and not ('0' in num_str_1 or '4' in num_str_1 or '6' in num_str_1 or '8' in num_str_1) and (num_1 in is_prime_set or is_prime(num_1))
        
        if is_truncatable_candidate_0:
            if all_primes(num_str_0):
                is_prime_set.add(num_0)
                primes.append(num_0)
        else:
            not_prime_set.add(num_0)
        
        if is_truncatable_candidate_1:
            if all_primes(num_str_1):
                is_prime_set.add(num_1)
                primes.append(num_1)
        else:
            not_prime_set.add(num_1)

        num += 6
    
    return primes, sum(primes)

def is_right_truncatable(num):
    for i in range(1, floor(log10(num))+1):
        if not is_prime( floor(num / (10 ** i)) ):
            return False
    return True

def compute2():
    left_truncatable_primes = []

    def make_left_truncatables(prime):
        # largest two-sided truncatable prime is 739397 (Wiki)
        if prime > 739_397: return
        
        for i in [1, 2, 3, 5, 7, 9]:
            prime_i = prime + i * 10 ** (floor(log10(prime)) + 1)
            if is_prime(prime_i):
                left_truncatable_primes.append(prime_i)
                make_left_truncatables(prime_i)

    make_left_truncatables(3)
    make_left_truncatables(7)

    truncatable_primes = sorted([prime for prime in left_truncatable_primes if is_right_truncatable(prime)])

    return truncatable_primes, sum(truncatable_primes)


if __name__ == '__main__':
    start1 = time.time()
    print(compute1())
    print(time.time() - start1)
    start2 = time.time()
    print(compute2())
    print(time.time() - start2)