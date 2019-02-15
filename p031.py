# dynamic programming, bottom-up
def compute():
    target = 200
    ways = {i:1 for i in range(target+1)}
    coin_amount = [2, 5, 10, 20, 50, 100, 200]
    
    for amount in coin_amount:
        for sum_ in range(amount, target+1):
            ways[sum_] += ways[sum_ - amount]
    
    return ways[target]

if __name__ == '__main__':
    print(compute())