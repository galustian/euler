import time
from util import is_prime

def compute():
    largest = 953
    largest_len = 21

    prime_table = [2, 3]
    for i in range(5, 45570, 6):
        if is_prime(i): prime_table.append(i)
        if is_prime(i+2): prime_table.append(i+2)

    for i in range(len(prime_table)):
        prime_sum = sum(prime_table[i:i+largest_len+1])

        for sum_len in range(largest_len+1, len(prime_table)):
            if sum_len == largest_len+1 and prime_sum > 999_999: return largest, largest_len
            if prime_sum > 999_999: break
            
            if is_prime(prime_sum):
                largest, largest_len = prime_sum, sum_len

            prime_sum += prime_table[i+sum_len]


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)