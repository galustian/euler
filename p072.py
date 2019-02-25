from number_theory.util import compute_all_phis

def compute():
    return sum(compute_all_phis(10**6)) - 1

if __name__ == '__main__':
    print(compute())
