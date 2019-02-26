from math import ceil, floor, gcd

def compute():
    gcd_1 = 0
    for den in range(4, 12001):
        print("Denominator:", den)
        for num in range(ceil(den/3), floor(den/2)+1):
            if gcd(num, den) == 1:
                gcd_1 += 1
        
    return gcd_1


if __name__ == '__main__':
    print(compute())
