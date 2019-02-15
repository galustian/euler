# n_s => list of consecutive results for the quadratic equation
def gauss_elimination_for_quad_equation(n_s=None):
    if len(n_s) != 3: raise ValueError("length of n_s must be 3")
    len_n = len(n_s)
    # ax^2 + bx + c = n
    n_s.append(n_s[0])
    del n_s[0]
    a_s = [x**2 for x in range(1, len_n)]
    a_s.append(0)
    b_s = list(range(1, len_n))
    b_s.append(0)
    c_s = [1] * len_n
    # echelon form
    for col_i, col in enumerate([a_s, b_s]):
        for row_i in range(col_i+1, len_n):
            x = col[row_i] / col[col_i]
            
            a_s[row_i] -= x * a_s[col_i]
            b_s[row_i] -= x * b_s[col_i]
            c_s[row_i] -= x * c_s[col_i]
            n_s[row_i] -= x * n_s[col_i]
    # reduced echelon form
    for col_i, col in enumerate([c_s, b_s]):
        for row_i in reversed(range(len_n-1-col_i)):
            x = col[row_i] / col[len_n-1-col_i]
            
            c_s[row_i] -= x * c_s[len_n-1-col_i]
            b_s[row_i] -= x * b_s[len_n-1-col_i]
            n_s[row_i] -= x * n_s[len_n-1-col_i]
    
    a, b, c = n_s[0] / a_s[0], n_s[1] / b_s[1], n_s[2] / c_s[2]
    return a, b, c

# a, b, c = gauss_elimination_for_quad_equation([1, 3, 13])
# print(a, b, c)
# def func(a, b, c, x=0): return a*(x**2) + b*x + c
# for i in range(10): print(func(a, b, c, x=i))

# this can be simplified even more and solved by hand
def compute():
    total_sum = 0
    for x in range(1, 501):
        total_sum += 4*(x**2) + x + 1
    return 4 * total_sum + 1


if __name__ == '__main__':
    print(compute())