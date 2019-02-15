import math
from util import next_largest_prime

class Number:
    def __init__(self, n):
        self.number = n
        self.prime_factors = {}
        self.prime_factorization()
    
    def prime_factorization(self):        
        self.prime_factors = {}
        
        num = self.number

        for p in next_largest_prime():
            if p > num: break
            
            n_times_p = 0
            while num % p == 0:
                num /= p
                n_times_p += 1
            
            self.prime_factors[p] = n_times_p
    
    def __mul__(self, n):
        self.number *= n
        self.prime_factorization()
        return self
    
    def __rmul__(self, n):
        self.number *= n
        self.prime_factorization()
        return self


def compute():
    n = Number(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
    # check if n has just enough prime-factors for all numbers from 2 to 20
    for i in range(2, 21):
        i = Number(i)        
        # if more certain prime-factors required, multiply by necessary amounts
        for p in i.prime_factors:
            if n.prime_factors[p] < i.prime_factors[p]:
                n *= p ** (i.prime_factors[p] - n.prime_factors[p])
                
    return n.number

if __name__ == '__main__':
    print(compute())
