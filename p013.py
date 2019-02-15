if __name__ == '__main__':
    with open('p013.txt') as f:
        # all numbers have to be taken into account... trivial problem...
        numbers = [int(line.rstrip('\n')) for line in f]    
    
    print(str(sum(numbers))[:10])
