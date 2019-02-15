from operator import mul
from functools import reduce
import multiprocessing as mp


def check_vertical(grid, largest_product):
    i_start = 0
    for col_i in range(len(grid)):
        while i_start + 3 <= len(grid)-1:
            i_end = i_start + 3
            
            product = reduce(mul, [grid[x][col_i] for x in range(i_start, i_end)])
            if product > largest_product.value:
                largest_product.value = product
            
            larger_i = False
            for i in range(1, len(grid) - i_start - 3):
                if grid[i_start + i][col_i] < grid[i_end + i][col_i]:
                    i_start = i_start + i
                    larger_i = True
                    break
        
            if not larger_i: break


def check_horizontal(grid, largest_product):
    i_start = 0
    for row_i in range(len(grid)):
        while i_start + 3 <= len(grid):
            i_end = i_start + 3
            
            product = reduce(mul, grid[row_i][i_start:i_end])
            if product > largest_product.value:
                largest_product.value = product
            
            larger_i = False
            for i in range(1, len(grid) - i_start - 3):
                if grid[row_i][i_start + i] < grid[row_i][i_end + i]:
                    i_start = i_start + i
                    larger_i = True
                    break
        
            if not larger_i: break


def check_diagonal1(grid, largest_product):
    for x_i in range(len(grid) - 4):
        for y_i in range(len(grid) - 4):
            product = grid[y_i][x_i] * grid[y_i+1][x_i+1] * grid[y_i+2][x_i+2] * grid[y_i+3][x_i+3]
            
            if product > largest_product.value:
                largest_product.value = product
            


def check_diagonal2(grid, largest_product):
    for x_i in range(3, len(grid)):
        for y_i in range(len(grid)-4):
            product = grid[y_i][x_i] * grid[y_i+1][x_i-1] * grid[y_i+2][x_i-2] * grid[y_i+3][x_i-3]
            
            if product > largest_product.value:
                largest_product.value = product
            

def compute(grid):
    largest_product = mp.Value('i', 0)
    
    processes = []
    for func in [check_vertical, check_horizontal, check_diagonal1, check_diagonal2]:
        # lock by default is true => data is automatically protected by a lock
        proc = mp.Process(target=func, args=(grid, largest_product))
        proc.start()
        processes.append(proc)

    for proc in processes: proc.join()

    return largest_product.value


if __name__ == '__main__':
    grid = []

    with open('p011.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split()
            line = [int(num) for num in line]
            grid.append(line)
    
    import time
    start = time.time()
    print(compute(grid))
    print(time.time() - start, "seconds")
