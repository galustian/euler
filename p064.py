import time
from math import floor, sqrt

def compute():
    odd_period_count = 0
    for i in range(2, 9999):
        if floor(sqrt(i))**2 == i: continue
        
        fraction_count = 0
        sqrt_, sqrt_c = sqrt(i), 0
        factor = 1
        variables = [(sqrt_c, factor)]
        
        # 1. add new fraction to fraction
        # 2. invert (sqrt_ - new fraction) and multiply times (sqrt_ + new fraction) to cancel sqrt_ in denominator
        # => factor and sqrt_c(=new fraction) get updated
        # => goto 1
        
        while True:
            fraction_count += 1
            
            frac_floor = (sqrt_ + sqrt_c) // factor
            sqrt_c -= factor * frac_floor
            factor = (i - sqrt_c**2) // factor # / factor => cancel-out prev factor # simplify: (sqrt_ - sqrt_c) * (sqrt_ + sqrt_c) / factor 
            sqrt_c *= -1

            if (sqrt_c, factor) in variables:
                if (fraction_count-1) % 2 == 1: odd_period_count += 1
                break
            
            variables.append((sqrt_c, factor))

    return odd_period_count

if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
