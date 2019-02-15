import time
from math import log10, floor

def compute1():
    current_number, extra_digit_steps = 1, 0
    
    digit_product, magnitude = 1, 1
    while magnitude < 1_000_000:
        current_number_magnitude = floor(log10(current_number)) + 1
        
        digit_steps_until_next_digit_magnitude = magnitude*9 # magnitude*10 - magnitude
        remainder_until_numbers_next_magnitude = 10 ** current_number_magnitude - current_number

        remainder_until_next_number = digit_steps_until_next_digit_magnitude // current_number_magnitude

        if remainder_until_next_number <= remainder_until_numbers_next_magnitude:
            current_number += remainder_until_next_number
        else:
            digit_steps_until_next_digit_magnitude -= remainder_until_numbers_next_magnitude * current_number_magnitude
            current_number += remainder_until_numbers_next_magnitude
            current_number_magnitude += 1
            current_number += digit_steps_until_next_digit_magnitude // current_number_magnitude
            
        extra_digit_steps += digit_steps_until_next_digit_magnitude % current_number_magnitude
        
        if extra_digit_steps >= current_number_magnitude:
            extra_digit_steps -= current_number_magnitude
            current_number += 1
            
        digit_product *= int(str(current_number)[extra_digit_steps])
        magnitude *= 10
    
    return digit_product
        

def compute2():
    num_str = ""
    i = 1
    while len(num_str) < 1_000_000:
        num_str += str(i)
        i += 1

    num, j = 1, 1
    while j <= 1_000_000:
        num *= int(num_str[j-1])
        j *= 10
    return num

if __name__ == '__main__':
    start1 = time.time()
    print(compute1())
    print(time.time() - start1)
    start2 = time.time()
    print(compute2())
    print(time.time() - start2)
