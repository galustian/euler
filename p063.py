from math import log10, floor

def compute():
    count = 0
    for num in range(1, 10):
        power, mgn = 1, floor(log10(num)+1)        
        while mgn == power:
            if mgn == power: count += 1
            power += 1
            mgn = floor(log10(num**power)+1)
    
    return count

if __name__ == '__main__':
    print(compute())
