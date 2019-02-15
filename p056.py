def compute():
    largest = 0
    # start with a=90, b=90
    for a in range(90, 100):
        if a % 10 == 0: continue
        for b in range(90, 100):
            power_sum = sum(map(int, str(a ** b)))
            if power_sum > largest: largest = power_sum

    return largest

if __name__ == '__main__':
    print(compute())
