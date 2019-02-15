from math import log2, floor

def palindrome_base2(n):
    base2_digits = floor(log2(n))
    for i in range(base2_digits):
        left_not_zero = n & (2 ** (base2_digits-i)) != 0
        right_not_zero = n & (2 ** i)
        if not ((left_not_zero and right_not_zero) or not (left_not_zero or right_not_zero)) : return False
        if i == base2_digits-i or i+1 == base2_digits-i: break
    return True

def palindrome(n):
    n_str = str(n)
    len_n_str = len(n_str)
    for i in range(0, len_n_str):
        if n_str[i] != n_str[len_n_str-1 - i]: return False
        if i == len_n_str-1 - i or i+1 == len_n_str-1 - i: break
    return True

def compute():
    sum_ = 0
    for i in range(1, 1_000_000, 2):
        if palindrome(i) and palindrome_base2(i):
            sum_ += i
    return sum_

if __name__ == '__main__':
    print(compute())