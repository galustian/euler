import time
from string import ascii_uppercase
from functools import reduce

def insertion_sort_str(str_arr):
    for i in range(1, len(str_arr)):
        for j in reversed(range(1, i+1)):
            if str_arr[j] < str_arr[j-1]:
                str_arr[j-1], str_arr[j] = str_arr[j], str_arr[j-1]    

# uses MSD (most-significant-digit-first) string sort
def compute(names):
    sorted_names = []

    def sort_string_array(name_arr, i=0):
        if len(name_arr) <= 40:
            insertion_sort_str(name_arr)
            sorted_names.extend(name_arr)
            return

        blank_ascii = '_' + ascii_uppercase

        for char in blank_ascii:
            sub_array = []
            for name in name_arr:
                if (name[i] if i < len(name) else '_') == char:
                    sub_array.append(name)

            if len(sub_array) > 0:
                sort_string_array(sub_array, i=i+1)

    sort_string_array(names)

    char_score = {char:i+1 for i, char in enumerate(ascii_uppercase)}
    total_score = 0
    for i, name in enumerate(sorted_names):
        total_score += (i+1) * sum([char_score[char] for char in name])

    return total_score

if __name__ == '__main__':
    all_names = []
    
    with open('p022.txt') as f:
        for line in f:
            line = line.rstrip('\n').rstrip(',')
            names = line.split(',')
            names = list(map(lambda n: n.strip('"'), names))
            all_names.extend(names)
    
    start = time.time()
    print(compute(all_names))
    print(time.time() - start)