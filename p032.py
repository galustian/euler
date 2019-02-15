import time
from math import floor, ceil, log10

def pandigital(x, y, z):
    digit_set = {digit for number in [x, y, z] for digit in str(number)}
    return len(digit_set) == 9

def has_digit_multiple_times(x):
    digit_set = {d for d in str(x)}
    return len(digit_set) != len(str(x))

def digit_size(x, y, product):
    return floor(log10(x)) + floor(log10(y)) + floor(log10(product)) + 3

def compute():
    products = set()
    for x in range(2, 101):
        if '0' in str(x) or has_digit_multiple_times(x): continue
        y = 10 ** (floor((9-floor(log10(x))-1) / 2) - 1)

        while digit_size(x, y, x*y) == 9:
            if '0' in str(y) + str(x*y):
                y += 1
                continue
            
            if pandigital(x, y, x*y):
                products.add(x*y)
                y += 1
                continue
            
            if digit_size(x, y, x*y) > 9: break
            y += 1
                    
    return products, sum(products)


if __name__ == '__main__':
    start = time.time()
    print(compute())
    print(time.time() - start)