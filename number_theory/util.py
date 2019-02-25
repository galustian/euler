from math import floor, sqrt
from functools import reduce
from operator import mul

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

def compute_all_phis(until):
    num_list = list(range(until+1))
    for i in range(2, len(num_list)):
        if num_list[i] == i:  # is prime
            for j in range(i, len(num_list), i):
                    num_list[j] -= num_list[j] // i

    return num_list

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

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def extended_euclidean(a, b):
    if b == 0: return a, 1, 0
    
    d, x, y = extended_euclidean(b, a % b)

    d, x, y = d, y, (x - (a//b) * y)

    return d, x, y


def coprime(a, b): 
    return gcd(a, b) == 1

# this algorithms follows from bezout's identity
# returns 0 if a and b not coprime
def modular_inverse(a, mod=2):
    d, x, y = extended_euclidean(a % mod, mod)
    if d != 1: return 0
    return x


def modular_exp(a, exp=1, mod=1):
    if exp <= 5:
        return (a**exp) % mod

    return (modular_exp(a, exp=exp//2, mod=mod) * modular_exp(a, exp=exp - exp//2, mod=mod)) % mod

# https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
def chinese_remainder(a_list=None, mod_list=None):
    result_x = 0
    
    Mod_Prod = reduce(mul, mod_list)
    for i in range(len(a_list)):
        Mi = Mod_Prod // mod_list[i]
        Mi_mod_inv = modular_inverse(Mi, mod=mod_list[i])
        result_x += a_list[i] * Mi * Mi_mod_inv

    return result_x


# n_s => list of consecutive results for the quadratic equation
# returns polynomial equation for generating consecutive values of n's
def gauss_elimination_for_quad_equation(n_s=None):
    if len(n_s) != 3: raise ValueError("length of n_s must be 3")
    len_n = len(n_s)
    # ax^2 + bx + c = n
    n_s.append(n_s[0]); del n_s[0]
    a_s = [x**2 for x in range(1, len_n)]; a_s.append(0)
    b_s = list(range(1, len_n)); b_s.append(0)
    c_s = [1] * len_n
    # echelon form
    for col_i, col in enumerate([a_s, b_s]):
        for row_i in range(col_i+1, len_n):
            x = col[row_i] / col[col_i]
            
            a_s[row_i] -= x * a_s[col_i]
            b_s[row_i] -= x * b_s[col_i]
            c_s[row_i] -= x * c_s[col_i]
            n_s[row_i] -= x * n_s[col_i]
    # reduced echelon form
    for col_i, col in enumerate([c_s, b_s]):
        for row_i in reversed(range(len_n-1-col_i)):
            x = col[row_i] / col[len_n-1-col_i]
            
            c_s[row_i] -= x * c_s[len_n-1-col_i]
            b_s[row_i] -= x * b_s[len_n-1-col_i]
            n_s[row_i] -= x * n_s[len_n-1-col_i]
    
    a, b, c = n_s[0] / a_s[0], n_s[1] / b_s[1], n_s[2] / c_s[2]
    return a, b, c


def continued_fraction_representation(i):
    fractions = []
    sqrt_, sqrt_c = sqrt(i), 0
    factor = 1
    variables = [(sqrt_c, factor)]
    
    while True:
        frac_floor = (sqrt_ + sqrt_c) // factor
        sqrt_c -= factor * frac_floor
        factor = (i - sqrt_c**2) // factor # / factor => cancel-out prev factor # simplify: (sqrt_ - sqrt_c) * (sqrt_ + sqrt_c) / factor 
        sqrt_c *= -1
        fractions.append(frac_floor)

        if (sqrt_c, factor) in variables: return fractions      
        variables.append((sqrt_c, factor))
