from util import gen_prime_table

def compute():
    return len({a**b for a in range(2, 101) for b in range(2, 101)})

if __name__ == '__main__':
    print(compute())