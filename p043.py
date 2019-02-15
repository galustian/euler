import time
from util import digit_list_to_num

def unique_digits(n):
    digit_s = str(n)
    digit_set = set(list(digit_s))
    return len(digit_set) == len(digit_s)

# backtracking
def compute():
    div_by = [2, 3, 5, 7, 11, 13, 17]
    
    def add_pandigital(div_by_i=0, starts_with=0, exclusion=None, pandigitals=[]):
        div = div_by[div_by_i]
        for i in range(10):
            if (starts_with*10 + i) % div == 0 and i not in exclusion:
                if div == 17:
                    pandigitals.append(digit_list_to_num(exclusion + [i]))
                    return
                else:
                    add_pandigital(div_by_i+1, (starts_with%10)*10 + i, exclusion + [i], pandigitals)
    
    # number is 1 billion or 2 ...
    pandigitals_list = []
    for i in range(1, 10):
        for j in range(102, 1000, 2):
            if unique_digits(j) and str(i) not in str(j):
                add_pandigital(div_by_i=1, starts_with=j%100, exclusion=[i, (j//100), (j//10)%10, j%10], pandigitals=pandigitals_list)
    
    return pandigitals_list, sum(pandigitals_list)


if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
