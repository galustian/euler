from util import next_largest_prime

def compute():
    large_number = 600851475143
    
    prev_prime = 0
    for prime in next_largest_prime():
        if prime > large_number:
            return prev_prime
        
        while large_number % prime == 0:
            large_number /= prime
        
        prev_prime = prime
        
if __name__ == '__main__':
    print(compute())