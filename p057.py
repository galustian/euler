from math import log10, floor

def compute():
    count = 0
    num, den = 1, 2
    for i in range(1, 1000):
        if floor(log10(num+den)+1) > floor(log10(den)+1): count += 1
        num_cache, num = num, den
        den = num_cache + 2 * den
    return count

if __name__ == '__main__':
    print(compute())
