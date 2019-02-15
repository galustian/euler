import math

def compute():
    right, down = 20, 20
    
    f = math.factorial
    return f(right + down) // f(right) // f(down)
    
if __name__ == '__main__':
    print(compute())