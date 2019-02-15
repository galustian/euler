#include <iostream>
#include <vector>

using namespace std;

// the Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given limit
// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
long compute() {
    int limit = 2000000;
    vector<int> sieve_primes {2};

    for (int x = 3; x < limit; x+=2) {
        bool is_prime = true;
        
        for (int p: sieve_primes) {
            if (p * p > x) break;
            if (x % p == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) sieve_primes.push_back(x);
    }

    long sum = 0;
    for (int p: sieve_primes) sum += p;
    return sum;
}

int main() {
    cout << compute() << endl;
}