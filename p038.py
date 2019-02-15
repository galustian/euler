import time

def decrement_no_duplicates(digit_list):
    for i in reversed(range(4)):
        if digit_list[i] != 0:
            digit_list[i] -= 1
            return
        elif digit_list[i] == 0 and i != 0:
            digit_list[i:] = [9] * (4 - i)
    
    if len(set(digit_list)) != 4:
        decrement_no_duplicates(digit_list)

def digit_list_double(digit_list):
    new_list = [0] * 5
    new_list[1:] = digit_list
    carry = 0
    for i in reversed(range(5)):
        new_val = new_list[i] * 2 + carry
        new_list[i], carry = new_val % 10, new_val // 10
    return new_list

def compute():
    current = [9, 8, 7, 6]

    distinct_digits = set(current + digit_list_double(current))
    while len(distinct_digits) != 9:
        decrement_no_duplicates(current)
        distinct_digits = set(current + digit_list_double(current))
        distinct_digits.discard(0)
    
    pandigital_list = current + digit_list_double(current)
    return sum([pandigital_list[i] * 10**(9-1-i) for i in range(len(pandigital_list))])
    
if __name__ == '__main__':
    start = time.time()
    print(compute())
    print(time.time() - start)