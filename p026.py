from util import is_prime

def inverse_number_repetend_length(denominator):
    remainders = [10]
    r_i = 0

    while (remainders[r_i] % denominator) * 10 not in remainders:
        remainders.append((remainders[r_i] % denominator) * 10)
        r_i += 1
    
    return len(remainders)

def compute():
    for n in reversed(range(7, 999)):
        if is_prime(n) and inverse_number_repetend_length(n) == n - 1:
            return n

if __name__ == '__main__':
    print(compute())