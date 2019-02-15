from util import next_largest_prime, is_prime

def compute_efficient_1():
    i = 0
    for p in next_largest_prime():
        i += 1
        if i == 10001:
            return p

def compute_efficient_2():
    nth = 10001
    n = 1 # 2 is prime, we begin with 3
    i = 1
    while n != nth:
        i += 2
        if is_prime(i):
            n += 1
    
    return i

if __name__ == '__main__':
    print(compute_efficient_1())
    print(compute_efficient_2())