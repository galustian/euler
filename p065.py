def compute_fraction(i, num=0, den=1):
    if i == -1: return num + 2*den, den
    frac = 2*((i-1)//3)+2 if (i-1) % 3 == 0 else 1
    return compute_fraction(i-1, num=den, den=frac*den + num) # swap num. and den. for next recursion step (1 / num/den = den/num)

if __name__ == '__main__':
    num, den = compute_fraction(100-2) # - 2 because first one starts at -1 (-1, 0, 1 ...)
    print( sum( map(int, str(num))) )
