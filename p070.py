from math import sqrt, floor
from numba import njit, jit

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

@njit
def get_phi(num, prime_exp_i_notzero_set):
    for i in prime_exp_i_notzero_set:
        num *= 1 - 1/prime_list[i]
    return num

def compute_all_phis(until):
    num_list = list(range(until+1))
    for i in range(2, len(num_list)):
        if num_list[i] == i:  # is prime
            for j in range(i, len(num_list), i):
                    num_list[j] -= num_list[j] // i

    return num_list

def is_perm(n1, n2):
    return sorted(list(str(n1))) == sorted(list(str(n2)))

def compute():
    eulers_phi = compute_all_phis(10**7)
    
    min_n = 2
    min_ratio_n = 2**20
    
    for n in range(3, 10**7):
        phi_n = eulers_phi[n]
        if phi_n == -1: continue
        if is_perm(n, phi_n) and n / phi_n < min_ratio_n:
            min_n = n
            min_ratio_n = n / phi_n

    return min_n



if __name__ == '__main__':
    print(compute())
