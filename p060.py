from util import is_prime
from math import floor, log10

def compute():
    prime_table = [i for i in range(3, 10_000, 2) if is_prime(i)]; del prime_table[1]
    prime_set, not_prime_set = set(prime_table), set()

    def concat_perms_are_prime(perm_primes, prime):
        for perm_p in perm_primes:
            prime_1 = 10**floor(log10(prime)+1)*perm_p + prime
            prime_2 = 10**floor(log10(perm_p)+1)*prime + perm_p

            is_prime_1 = prime_1 in prime_set or (prime_1 not in not_prime_set and is_prime(prime_1))
            is_prime_2 = prime_2 in prime_set or (prime_2 not in not_prime_set and is_prime(prime_2))
            if is_prime_1:
                prime_set.add(prime_1)
                if is_prime_2: prime_set.add(prime_2)
                else: not_prime_set.add(prime_2)
            else: not_prime_set.add(prime_1)

            if not (is_prime_1 and is_prime_2): return False
        return True

    def prime_permutations(prime_i, perm_primes=None):
        for i in range(prime_i, len(prime_table)):
            prime = prime_table[i]

            if perm_primes == None:
                result = prime_permutations(prime_i+1, perm_primes=[prime])
                if result != None: return result
            else:
                if concat_perms_are_prime(perm_primes, prime):
                    if prime_i == 4: return perm_primes + [prime], sum(perm_primes)+prime
                    
                    result = prime_permutations(prime_i+1, perm_primes=perm_primes + [prime])
                    if result != None: return result
        
        return None

    return prime_permutations(0)

if __name__ == '__main__':
    print(compute())
