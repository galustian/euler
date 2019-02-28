from math import sqrt, floor, gcd
import time

SIZE = 750_000

def compute():
    wire_lengths, wire_lengths_2 = [0] * (SIZE+1), [0] * (SIZE+1)
    
    for m in range(2, floor(sqrt(SIZE)) + 1):
        for n in range(1 if m%2==0 else 2, m, 2):
            if gcd(n, m) != 1: continue
            
            l = m*(m + n)
            if l > SIZE: break
            wire_lengths[l] += 1            
            
            for k in range(2, floor(SIZE / l) + 1):
                wire_lengths_2[l * k] += 1
    
    return sum(1 for i in range(SIZE) if wire_lengths[i] + wire_lengths_2[i] == 1)


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
