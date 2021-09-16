from collections import Counter

n = int(input())
sequence = [1, 1]
new_sequence = []

for step in range(n-1):
    for index in range(len(sequence[:-1])):
        new_sequence.append(sequence[index])
        new_sequence.append(sequence[index]+sequence[index+1])
    new_sequence.append(sequence[-1])

    print(sequence, step+1, Counter(sequence)[step+1])

    sequence, new_sequence = new_sequence, []

print(sequence, step+2, Counter(sequence)[step+2])

# TODO...
