import time
from math import log10, floor

def magnitude(n): return floor(log10(n)+1) if n != 0 else 0
def gen_figurate_numbers(func):
    nums = {}
    for i in range(10, 10_000):
        n = func(i)
        if n > 9999: return nums
        if n > 1000 and magnitude(n % 100) > 1:
            if n//100 not in nums: nums[n//100] = [n]
            else: nums[n//100].append(n)

def compute():
    figurate_numbers = []
    figurate_numbers.append(gen_figurate_numbers(lambda x: x*(3*x-2)))
    figurate_numbers.append(gen_figurate_numbers(lambda x: x*(5*x-3)//2))
    figurate_numbers.append(gen_figurate_numbers(lambda x: x*(2*x-1)))
    figurate_numbers.append(gen_figurate_numbers(lambda x: x*(3*x-1)//2))
    figurate_numbers.append(gen_figurate_numbers(lambda x: x**2))
    figurate_numbers.append(gen_figurate_numbers(lambda x: x*(x+1)//2))

    def depth_first(starts_with=None, exclude_i="", numbers=None):
        if starts_with == None:
            for starts_with in figurate_numbers[0]:
                for num in figurate_numbers[0][starts_with]:
                    result = depth_first(num%100, exclude_i="0", numbers=[num])
                    if result != None: return result
        else:
            if len(exclude_i) == 6:
                if numbers[5]%100 == numbers[0]//100: return numbers
                return None

            for i, fig_nums in enumerate(figurate_numbers):
                if starts_with not in fig_nums or str(i) in exclude_i: continue
                
                for num in fig_nums[starts_with]:
                    result = depth_first(num%100, exclude_i=exclude_i+str(i), numbers=numbers + [num])
                    if result != None: return result

            return None

    return depth_first()

if __name__ == '__main__':
    start = time.process_time()
    result = compute()
    print(result, sum(result))
    print(time.process_time() - start)
