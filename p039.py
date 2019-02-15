import time
from math import sqrt, floor, gcd
from collections import Counter

def compute():
    # Pythagorean Triples:
    # a = m² - n² | b = 2mn | c = m² + n²
    # m < sqrt(p / 2)
    # p = 2m * (m + n)
    perimeters = []

    for m in range(1, floor(sqrt(1000 / 2)) + 1):
        for n in range(1, m+1):
            if gcd(m, n) == 1:
                p = 2*m*(m+n)
                # maximum: p * k = 1000 => k = 1000 / p
                perimeters.extend([p*k for k in range(1, floor(1000/p)+1)])
    
    return Counter(perimeters).most_common(1)[0]


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
