import time
from util import is_prime


def create_additions(num_str, digit_str):
    digit_magnitude = [len(num_str)-1-i for i in range(len(num_str)-1) if num_str[i] == digit_str]

    additions = []
    for i in range(1, 2**len(digit_magnitude)):
        binary = bin(i)[2:]
        add = sum( int(binary[-di]) * 10**digit_magnitude[-di] for di in range(1, len(binary)+1) )
        additions.append(add)

    return additions


def check_digit_replacement(num, digit):
    additions = create_additions(str(num), str(digit))

    for add in additions:
        prime_count = 1
        for i in range(1, 10 - digit):
            if is_prime(num + add * i): prime_count += 1
            if prime_count + (9 - digit - i) < 8: break # even if all other i's were primes => not sufficient

        if prime_count >= 8: return True
    
    return False


def compute():
    prime = 56005
    while True:
        prime += 2
        if not is_prime(prime): continue
        prime_str = str(prime)
        if '0' in prime_str:
            if check_digit_replacement(prime, 0): return prime
    
        if '1' in prime_str:
            if check_digit_replacement(prime, 1): return prime
    
        if '2' in prime_str:
            if check_digit_replacement(prime, 2): return prime
        


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
