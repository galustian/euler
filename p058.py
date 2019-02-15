from number_theory.util import gauss_elimination_for_quad_equation, is_prime

def quad(x, a, b, c): return a*x**2 + b*x + c

def compute():
    a1, b1, c1 = gauss_elimination_for_quad_equation([3, 13, 31])
    a2, b2, c2 = gauss_elimination_for_quad_equation([5, 17, 37])
    a3, b3, c3 = gauss_elimination_for_quad_equation([7, 21, 43])

    x = 0
    primes, not_primes = 0, 1
    while primes * 10 >= primes + not_primes or primes == 0:
        diag = quad(x, a1, b1, c1), quad(x, a2, b2, c2), quad(x, a3, b3, c3)
        for num in diag:
            if is_prime(num): primes += 1
            else: not_primes += 1
        not_primes += 1 # bottom right
        x += 1 
    
    return x*2 + 1

if __name__ == '__main__':
    print(compute())
