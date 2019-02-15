import math

def formula(a, b):
    return 1000 * math.sqrt(a*a + b*b) + a*b

def compute():
    # one can prove that a and b must satisfy
    # 1000 * sqrt(a*a + b*b) + a*b = 500.000
    # and a and b must be < 500 because a < c and b < c
    # TODO maybe: use euclids formula
    for a in range(500):
        for b in range(500):
            if int(formula(a, b)) == 500_000:
                return a * b * int(math.sqrt(a*a + b*b))

if __name__ == '__main__':
    print(compute())
