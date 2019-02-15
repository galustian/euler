from util import is_prime, digit_list_to_num
import time

def combinations_with_new_digit(d, combinatinons):
    combinatinons_with_d = []
    
    for comb in combinatinons:
        for i in range(len(comb)+1):
            comb_with_d = comb[:i] + [d] + comb[i:]
            combinatinons_with_d.append(comb_with_d)

    return combinatinons_with_d

def all_combinations(a):
    if len(a) == 1: return [a]
    return combinations_with_new_digit(a[0], all_combinations(a[1:]))

def compute():
    # adding 8 or 9 will make sum of digits divisible by 3 => number is divisible by 3    
    digits = [1, 2, 3, 4, 5, 6, 7]
    combs = all_combinations(digits)
    prime_combs = [c for c in combs if is_prime(digit_list_to_num(c))]
    return digit_list_to_num(max(prime_combs))


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
