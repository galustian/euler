from math import factorial

def digit_factorial_sum(n):
    return sum(map(factorial, map(int, list(str(n)))))

def compute():
    chain_length = {}
    len_60 = 0
    
    for chain_num in range(1, 10**6):
        num_chain, nums_in_chain = [], set()

        loop_num_idx = 10**10
        while True:
            if chain_num in chain_length:
                num_chain.extend([-1] * chain_length[chain_num])
                break
            if chain_num in nums_in_chain:
                loop_num_idx = num_chain.index(chain_num)
                break
            
            num_chain.append(chain_num)
            nums_in_chain.add(chain_num)
            chain_num = digit_factorial_sum(chain_num)
        
        for i in range(len(num_chain)):
            if num_chain[i] == -1: break        
            loop_length = len(num_chain) - i if i < loop_num_idx else len(num_chain) - loop_num_idx

            if loop_length == 60 and num_chain[i] < 1_000_000 and num_chain[i] not in chain_length:
                len_60 += 1
            
            chain_length[num_chain[i]] = loop_length
        
    return len_60

if __name__ == '__main__':
    print(compute())
