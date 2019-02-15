from math import floor
from string import ascii_uppercase

def compute():
    triangle_numbers = {floor(n*(n+1)/2) for n in range(30)}
    letter_value = {ascii_uppercase[i-1]:i for i in range(1, len(ascii_uppercase)+1)}

    with open('p042.txt') as f:
        text = f.read()
        word_list = [word.strip('"') for word in text.split(',')]

    triangle_count = 0
    for word in word_list:
        word_value = sum(letter_value[l] for l in word)
        if word_value in triangle_numbers: triangle_count += 1
    
    return triangle_count

if __name__ == '__main__':
    print(compute())