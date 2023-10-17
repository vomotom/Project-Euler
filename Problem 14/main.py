# Longest Collatz Sequence

import time

def get_collatz_sequence(starting_number):
    current_number = starting_number
    sequence = [starting_number]
    while current_number > 1:
        # if even
        if current_number % 2 == 0:
            current_number = int(current_number / 2)
        # if odd
        else:
            current_number = 3 * current_number + 1
        sequence.append(current_number)
    return(sequence)

print(get_collatz_sequence(13))

start = time.time()
longest_sequence = 0
longest_sequence_number = 1
i = 1
while time.time() - start <= 60:
    length = len(get_collatz_sequence(i))
    if length > longest_sequence:
        longest_sequence = length
        longest_sequence_number = i
        print(f"Number: {longest_sequence_number}, Sequence length: {longest_sequence}")
    i += 1

print("Finished!")


    
