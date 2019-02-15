def one_to_99():
    one_to_9 = 36
    ten_to_19 = 70
    
    total = 9 * one_to_9 + ten_to_19
    total += 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6)

    return total

def compute():
    total = one_to_99() * 10

    one_to_9 = 36

    ones = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)
    # ___ hundred and
    total += 9 * 99 * 3
    # one hundred ..., two hundred ...
    total += 900 * 7 + 100 * one_to_9

    return total + len("onethousand")

if __name__ == '__main__':
    print(compute())