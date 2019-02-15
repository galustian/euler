import time
from math import log10, floor
from util import is_prime

def digit_permutations(num_str):
    if len(num_str) == 1: return [num_str]
    
    permutations = []
    for i in range(len(num_str)):
        sub_permutations = digit_permutations(num_str[:i] + num_str[i+1:])
        for perm in sub_permutations:
            permutations.append(num_str[i] + perm)

    return permutations

def compute():
    prime_list = [i for i in range(1001, 9999) if is_prime(i)]
    prime_set = set(prime_list)

    for p in prime_list:
        if p not in prime_set: continue

        permutations = list(set(map(int, digit_permutations(str(p)))))
        
        prime_perms = [perm for perm in permutations if floor(log10(perm))+1 == 4 and is_prime(perm)]
        if len(prime_perms) < 3:
            for prime in prime_perms: prime_set.remove(prime)
            continue
        prime_perms = sorted(prime_perms)

        for i in range(len(prime_perms)-2):
            if prime_perms[i+1] - prime_perms[i] == prime_perms[i+2] - prime_perms[i+1]:
                return str(prime_perms[i]) + str(prime_perms[i+1]) + str(prime_perms[i+2])
        
        for perm in prime_perms: prime_set.remove(perm)


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
