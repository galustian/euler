from math import floor, sqrt

# this method uses the fact that every prime > 3 can be written as 6k +- 1
# and that every number n must at least have one prime-factor less than sqrt(n)
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False

    bound = floor(sqrt(n))

    for i in range(5, bound+1, 6):
        if n % i == 0:
            return False
        if n % (i+2) == 0:
            return False
    
    return True


def next_largest_prime():
    n = 2
    yield n
    n -= 1

    while True:
        n += 2
        
        if is_prime(n):
            yield n

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def gen_prime_table(bound):
    primes = [2, 3]

    for i in range(5, bound+1, 6):
        prime1, prime2 = True, True
        for p in primes:
            if p > sqrt(i): break
            if i % p == 0:
                prime1 = False
        
        for p in primes:
            if p > sqrt(i+2): break
            if (i+2) % p == 0:
                prime2 = False
        
        if prime1: primes.append(i)
        if prime2: primes.append(i+2)

    return primes        


def is_pandigital(n):
    all_digits, digit_count = 0, 1
    while n >= 1:
        all_digits ^= 1 << (n % 10)
        n //= 10
        digit_count += 1
    return all_digits == (1 << digit_count) - 2 # - 1 => 11111 | - 2 => 11110 (no zeros allowed in pandigital numbers)


def digit_in_num(n):
    pass

def digit_list_to_num(num_list):
    return int(''.join(map(str, num_list)))