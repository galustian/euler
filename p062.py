import time
from math import log10, floor

def lists_have_same_values(list1, list2):
    pass

def compute():
    cubes_magnitude_sorted = {i:[] for i in range(2, 15)}
    cubes_magnitude = {i:[] for i in range(2, 15)}

    for i in range(1000, 10000):
        cubes_magnitude_sorted[floor(log10(i)+1)].append( sorted(map(int, str(i**3))) )
        cubes_magnitude[floor(log10(i)+1)].append( list(map(int, str(i**3))) )

    for mgn in range(2, 20):
        for i, cube_digits in enumerate(cubes_magnitude_sorted[mgn]):
            if cubes_magnitude_sorted[mgn].count(cube_digits) == 5:
                return int(''.join(map(str, cubes_magnitude[mgn][i])))

if __name__ == '__main__':
    start = time.process_time()
    print(compute())
    print(time.process_time() - start)
