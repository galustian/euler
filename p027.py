import time
from util import next_largest_prime, is_prime

def compute():
    longest_sequence = 0
    best_a, best_b = 0, 0

    for b in next_largest_prime():
        if b > 999: break
        a_lower_bound = 1 - b - 1 # extra -1 at end so that a is always odd

        for a in range(a_lower_bound, 1000, 2):
            n = 0
            fx = n**2 + a*n + b
            while fx > 1 and is_prime(fx):
                n += 1
                fx = n**2 + a*n + b
            if n > longest_sequence:
                longest_sequence = n
                best_a, best_b = a, b
    
    return best_a, best_b, longest_sequence


if __name__ == '__main__':
    start = time.time()
    best_a, best_b, longest_sequence = compute()
    print("a =", best_a, "b =", best_b, "longest sequence:", longest_sequence)
    print("Product:", best_a * best_b)
    print(time.time() - start)