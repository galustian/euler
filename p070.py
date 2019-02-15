from math import sqrt, floor
from functools import reduce
from operator import mul
from numba import jit

prime_list = None


@jit(nopython=True)
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

    for i in range(5, floor(sqrt(n))+1, 6):
        if n % i == 0: return False
        if n % (i+2) == 0: return False
    return True


def is_perm(n1, n2):
    return sorted(list(str(n1))) == sorted(list(str(n2)))


def get_num(primes, prime_exp):
    prime_with_exp = [primes[i] ** prime_exp[i] for i in range(len(primes))]
    return reduce(mul, prime_with_exp)


def phi(primes, num):
    for p in primes:
        num *= 1 - 1 / p
    return int(num)


def increment_prime_list(primes, prime_exp, max_size=90_000):
    i = 0
    prime_exp[i] += 1
    while get_num(primes, prime_exp) > max_size:
        if i == len(primes)-1:
            primes.append(prime_list[i+1])
            prime_exp.append(0)

        prime_exp[i] = 0 # set previous prime exponent to 0
        prime_exp[i+1] += 1 # increment current prime exponent

        i += 1


def compute():
    phi_primes = [prime_list[0]]
    phi_prime_exp = [1]
    
    while True:
        num = get_num(phi_primes, phi_prime_exp)        
        phi_num = phi([phi_primes[i] for i in range(len(phi_primes)) if phi_prime_exp[i] != 0], num)
        if is_perm(phi_num, num):
            print(phi_num)
            return num

        increment_prime_list(phi_primes, phi_prime_exp)


if __name__ == '__main__':
    # Todo: lazy prime-generation
    prime_list = [i for i in reversed(range(3, 9_000, 2)) if is_prime(i)] + [2]
    print(compute())
