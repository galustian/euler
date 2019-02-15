from util import is_prime, gen_prime_table
import time

start1 = time.process_time()
a = gen_prime_table(1000000)
print("Sieve:", time.process_time() - start1, len(a))

start2 = time.process_time()
b = [2, 3]
for i in range(5, 1000000, 6):
  if is_prime(i): b.append(i)
  if is_prime(i+2): b.append(i+2)
print("Loop6:", time.process_time() - start2, len(b))


start3 = time.process_time()
c = [2, 3]
for i in range(5, 1000000, 2):
  if is_prime(i): c.append(i)
print("Loop2:", time.process_time() - start3, len(c))