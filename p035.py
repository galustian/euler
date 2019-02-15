import time
from math import sqrt
from util import is_prime

def gen_prime_table(bound):
    primes = [2, 3, 5]

    for i in range(7, bound+1, 2):
        prime_str = str(i)
        if '0' in prime_str or '2' in prime_str or '4' in prime_str or '5' in prime_str or '6' in prime_str or '8' in prime_str:
            continue
        if is_prime(i): primes.append(i)

    return primes    

def permutations(n):
    n_str = str(n)
    perms = set()

    for i in range(len(n_str)):
        n_str += n_str[0]
        n_str = n_str[1:]
        perms.add(int(n_str))
    
    return sorted(list(perms))

def compute():
    prime_table = gen_prime_table(999_999)
    prime_set = set(prime_table)
    circular_list = []

    count = 0
    for prime in prime_table:
        if prime not in prime_set:
            continue
        
        perms = permutations(prime)

        is_circular = True
        for p in perms:
            if p in prime_set:                
                prime_set.remove(p)
            else:
                is_circular = False

        if is_circular:
            circular_list.extend(perms)
            count += len(perms)

    return count, sorted(circular_list)


if __name__ == '__main__':
    start = time.time()
    count, circular_list = compute()
    print(count)
    for p in circular_list: print(p)
    print(time.time() - start)
