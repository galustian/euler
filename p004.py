import math

def is_divisible_by_two_three_digit_numbers(num):
    # num < i * 1000
    for i in range(math.ceil(num/1000), 1000):
        if num % i == 0:
            return True
    return False

def compute():
    for digit in range(999, 99, -1):
        palindrome = int(str(digit) + str(digit)[::-1])
        if is_divisible_by_two_three_digit_numbers(palindrome):
            return palindrome

if __name__ == '__main__':
    print(compute())