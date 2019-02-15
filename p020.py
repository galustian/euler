import time

def compute():
    val = 1

    for i in range(2, 101):
        val *= i
        while val % 10 == 0:
            val //= 10

    return sum([int(d) for d in str(val)])

if __name__ == '__main__':
    print(compute())
