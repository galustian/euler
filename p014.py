# the convergence of this problem has been proven to be undecidable for ax + b
# using a clever memoization algorithm => very fast
def compute():
    number_sequence_length = {1: 1}
    longest_sequence, longest_sequence_n = 0, 0
    
    for n in range(2, 1_000_000):
        init_n = n
        
        if n in number_sequence_length: continue
        
        sequence_length = 1
        generated_numbers = [n]

        while True:
            if not n % 2:
                n = n // 2
                try:
                    sequence_length += number_sequence_length[n]

                    if sequence_length > longest_sequence:
                        longest_sequence, longest_sequence_n = sequence_length, init_n
                    
                    for i, gen_num in enumerate(generated_numbers):
                        number_sequence_length[gen_num] = sequence_length - i
                    
                    break

                except KeyError:
                    sequence_length += 1
                    generated_numbers.append(n)
            
            else:
                n = 3 * n + 1
                try:
                    sequence_length += number_sequence_length[n]

                    if sequence_length > longest_sequence:
                        longest_sequence, longest_sequence_n = sequence_length, init_n
                    
                    for i, gen_num in enumerate(generated_numbers):
                        number_sequence_length[gen_num] = sequence_length - i
                    
                    break

                except KeyError:
                    sequence_length += 1
                    generated_numbers.append(n)

    return longest_sequence_n


if __name__ == '__main__':
    import time
    start = time.time()
    print(compute())
    print(time.time() - start)