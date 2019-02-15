#include <iostream>

int compute_method1() {
    int prev = 1;
    int fib = 1;

    unsigned int sum = 0;

    while (fib <= 4000000) {
        if (fib % 2 == 0) 
            sum += fib;
        
        int prev_fib = fib;
        fib += prev;
        prev = prev_fib;
    }
    
    return sum;
}

int compute_method2() {
    int a = 1;
    int b = 1;
    int c = a + b;

    unsigned int sum = 0;

    while (c <= 4000000) {
        sum += c;
        a = b + c;
        b = a + c;
        c = b + a;
    }

    return sum;
}

int main() {
    std::cout << compute_method1() << std::endl;
    std::cout << compute_method2() << std::endl;
}