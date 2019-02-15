import time

def increment(number):
    if number[-1] != 9:
        number[-1] += 1
        return

    for i in reversed(range(0, len(number))):
        if number[i] == 9 and i == 0:
            number.append(0)
            number[0], number[1:] = 1, [0] * (len(number)-1)
        elif number[i] == 9:
            number[i] = 0
        else:
            number[i] += 1
            break


def to_number(number):
    num_str = ''
    for d in number:
        num_str += str(d)
    return int(num_str)


def pow_sum(number, power=5):
    sum_ = 0
    for d in number:
        sum_ += d**power
    return sum_


def compute():
    sum_numbers = []
    number = [1, 0]
    # 9**5 * 6 == 354294
    while to_number(number) < 354_295:    
        num = to_number(number)
        if num == pow_sum(number):
            sum_numbers.append(num)

        increment(number)

    return sum(sum_numbers), sum_numbers

if __name__ == '__main__':
    start = time.time()
    print(compute())
    print(time.time()-start)