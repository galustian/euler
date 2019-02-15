#include <iostream>
#include <math.h>

using namespace std;

#define SIZE 180

int compute() {
    int num[SIZE] = {};
    num[0] = 1;

    for (int i = 2; i < 100; i++) {
        int carry = 0;
        for (int j = 0; j < SIZE; j++) {
            int digit_with_carry = num[j] * i + carry;

            num[j] = digit_with_carry % 10;
            carry = digit_with_carry / 10;
        }
    }

    int sum = 0;
    for (int d: num) sum += d;
    return sum;
}

int main() {
    cout << compute() << endl;
    return 0;
}
