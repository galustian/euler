import time

def digit_product(number_str):
    if len(number_str) == 1:
        return int(number_str[0])
    return digit_product(number_str[1:]) * int(number_str[0])

def compute1():
    number_str = ''
    with open('p008.txt') as f:
        number_str = f.read()

    largest_product = 0

    i_end = 13
    while i_end <= len(number_str):
        i_start = i_end - 13

        if '0' in number_str[i_start:i_end]:
            i_end = number_str[:i_end].rfind('0') + 14
            continue
        
        product = digit_product(number_str[i_start:i_end])
        if product > largest_product:
            largest_product = product

        i_end += 1
        
    return largest_product

# slightly faster method
def compute2():
    number_str = ''
    with open('p008.txt') as f:
        number_str = f.read()

    largest_product = 0

    i_end = 13
    while i_end <= len(number_str):
        i_start = i_end - 13

        if '0' in number_str[i_start:i_end]:
            i_end = number_str[:i_end].rfind('0') + 14
            continue
        
        product = digit_product(number_str[i_start:i_end])
        if product > largest_product:
            largest_product = product

        if int(number_str[i_start]) >= int(number_str[i_end]) + 1:
            i_end += 2
        else:
            i_end += 1
        
    return largest_product

if __name__ == '__main__':
    start1 = time.time()
    print(compute1())
    print("seconds: {}".format(time.time() - start1))
    start2 = time.time()
    print(compute2())
    print("seconds: {}".format(time.time() - start2))