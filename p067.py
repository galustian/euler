def compute(top_bottom_list):
    for i in reversed(range(len(top_bottom_list)-1)):
        curr, below = top_bottom_list[i], top_bottom_list[i+1]
        for j in range(len(curr)):
            curr[j] += below[j] if below[j] > below[j+1] else below[j+1]
    return top_bottom_list[0][0]

if __name__ == '__main__':
    with open('p067.txt') as f:
        top_bottom_list = [list(map(int, l.strip().split(' '))) for l in f]
    print(compute(top_bottom_list))
