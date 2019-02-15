from math import sqrt, floor
from number_theory.util import continued_fraction_representation

def compute_fraction(rep, i, num=0, den=1):
    if i == 0: return floor(rep[0])*den + num, den
    return compute_fraction(rep, i-1, num=den, den=num + floor(rep[i])*den)

def compute():
    d, max_num = 0, 0
    for i in range(2, 1001):
        if floor(sqrt(i))**2 == i: continue
        
        fraction_repr = continued_fraction_representation(i)
        fraction_i = 2
        num, den = compute_fraction(fraction_repr[:fraction_i], len(fraction_repr[:fraction_i])-1)
        
        while num**2 - i*den**2 != 1:
            fraction_i += 1
            if fraction_i == len(fraction_repr):
                fraction_repr += fraction_repr[1:]
            num, den = compute_fraction(fraction_repr[:fraction_i], len(fraction_repr[:fraction_i])-1)
        
        if num > max_num:
            max_num = num
            d = i
        
    return d

if __name__ == '__main__':
    print(compute())
