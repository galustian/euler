from util import gen_prime_table

def compute():
    UPPER = 3
    primes = gen_prime_table(1000)
    Ways = [0] * UPPER
    Ways[0] = 1

    while True:
        for i in range(len(primes)):
            for n in range(primes[i], UPPER):
                Ways[n] += Ways[n - primes[i]]
                
                if Ways[n] > 5000: return n
        
        UPPER += 1
        Ways = [0] * UPPER
        Ways[0] = 1

    return -1

if __name__ == '__main__':
    print(compute())
