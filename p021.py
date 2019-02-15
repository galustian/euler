import time
from util import gen_prime_table, is_prime

prime_table = None

def prime_factorization(n):
    global prime_table
    
    if is_prime(n): return {n: 1}
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

def next_prime_factor_combination(prime_counts):
    combinations = [0] * len(prime_counts)
    yield combinations

    while combinations != prime_counts:
        carry = False
        for i in range(0, len(combinations)):
            if not carry:
                if combinations[i] == prime_counts[i]:
                    carry = True
                    continue
                else:
                    combinations[i] += 1
                    yield combinations
                    break
            
            if combinations[i] != prime_counts[i]:
                combinations[i] += 1
                combinations[:i] = [0] * i
                yield combinations
                break
            else:
                if i == len(combinations)-1: break # combinator fully incremented
                continue


# save all combinations of prime factors
def get_all_divisors(num):
    prime_factors = prime_factorization(num)
    primes = list(prime_factors.keys())
    prime_counts = list(prime_factors.values())

    all_divisors = set()
    
    for comb in next_prime_factor_combination(prime_counts):
        divisor = reduce(mul, [primes[i] ** comb[i] for i in range(len(comb))])
        all_divisors.add(divisor)

    all_divisors.remove(num)

    return all_divisors

# more efficient than get_all_divisors
# https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
def get_all_divisors_sum(num):
    prime_factors = prime_factorization(num)
    
    divisors_sum = 1
    for p, counts in prime_factors.items():
        divisors_sum *= (p ** (counts+1) - 1) // (p - 1)
    
    return divisors_sum - num


def compute():
    numbers_divisors_sum = {}

    amicable_sum = 0

    for num in range(220, 10000):
        num_divisors_sum = get_all_divisors_sum(num)
        try:
            if numbers_divisors_sum[num] == num_divisors_sum:
                amicable_sum += num + numbers_divisors_sum[num]
        except KeyError:
            numbers_divisors_sum[num_divisors_sum] = num

    return amicable_sum


if __name__ == '__main__':
    prime_table = gen_prime_table(4999)
    start = time.time()
    print(compute())
    print(time.time() - start)