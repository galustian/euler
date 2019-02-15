from string import ascii_lowercase

def gen_all_keys(depth):
    if depth == 1: return list(ascii_lowercase)
    new_keys = []
    for key in gen_all_keys(depth-1):
        for char in ascii_lowercase:
            new_keys.append(char + key)
    return new_keys

def decrypt(ascii_list, key):
    return ''.join(map(chr, [ascii_list[i] ^ ord(key[i % len(key)]) for i in range(len(ascii_list))]))

def compute(ascii_list):
    for key in gen_all_keys(3):
        text = decrypt(ascii_list, key)
        if ' the ' in text: return text

if __name__ == '__main__':
    with open('p059.txt') as f:
        ascii_list = list(map(int, f.read().split(',')))
    
    text = compute(ascii_list)
    print(sum(ord(char) for char in text))
    print(text)
