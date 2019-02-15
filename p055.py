import time

def palindrome(n): return int(str(n)[::-1])
def is_palindrome(n): return n == palindrome(n)

def compute():
    is_lychrel, no_lychrel = set(), set()

    for i in range(10, 10_000):
        if i in no_lychrel or i in is_lychrel: continue
        num, num_at_step = i, []
        is_lychrel_num = True
        
        for _ in range(50):
            num_at_step.append(num)
            num += palindrome(num)
            
            if is_palindrome(num):
                for n in num_at_step:
                    no_lychrel.add(n)
                    if n % 10 != 0: no_lychrel.add(palindrome(n))
                is_lychrel_num = False
                break

        if is_lychrel_num:
            is_lychrel.add(i)
            if i % 10 != 0: is_lychrel.add(palindrome(i))

    return sorted(list(is_lychrel)), len(is_lychrel)

if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
