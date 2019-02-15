N_RANGE = 1000

def compute_simple():
    sum_ = 0

    for i in range(N_RANGE):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i
    
    return sum_

def compute_inclusion_exclusion():
    sum_ = 0

    for i in range(N_RANGE):
        if i % 3 == 0:
            sum_ += i
    
    for i in range(N_RANGE):
        if i % 5 == 0:
            sum_ += i
    
    for i in range(N_RANGE):
        if i % 15 == 0:
            sum_ -= i
    
    return sum_

if __name__ == '__main__':
    print(compute_simple())
    print(compute_inclusion_exclusion())