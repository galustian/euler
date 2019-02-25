from math import floor, gcd

def compute():
    best_num, best_den = 2, 5
    best_ratio = best_num / best_den

    for den in reversed(range(9, 10**6+1)):
        closest_num = floor((3 * den) / 7)
        for num in reversed(range(closest_num+1)):
            if best_ratio >= num / den: break
            if not (num%2==0 and den%2==0) and gcd(num, den) == 1:
                best_num, best_den = num, den
                best_ratio = num / den

    return best_num

if __name__ == '__main__':
    print(compute())
