import math

# https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio
# https://en.wikipedia.org/wiki/Golden_ratio
def nth_fibonacci(n):
    G1 = (1 + math.sqrt(5)) / 2
    G2 = (1 - math.sqrt(5)) / 2
    return int((G1 ** n - G2 ** n) / math.sqrt(5))

# the G2 term ~ -0.61.. converges to 0 for large n
def nth_fibonacci_large(n):
    G1 = (1 + math.sqrt(5)) / 2
    return int(G1 ** n / math.sqrt(5))

if __name__ == '__main__':
    G1 = (1 + math.sqrt(5)) / 2
    
    nth_fib_with_1000_digits = (999 + math.log10(math.sqrt(5))) / math.log10(G1)
    print(nth_fib_with_1000_digits)