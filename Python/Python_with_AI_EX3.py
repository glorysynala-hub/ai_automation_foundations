L1 = [1, 2, 2, 3, 2, 3, 4, 5]

# Step 1: Count occurrences using dictionary
freq = {}

for item in L1:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Step 2: Find most repetitive element
max_count = 0
most_repetitive = None

for key, value in freq.items():
    if value > max_count:
        max_count = value
        most_repetitive = key

print("Most repetitive element:", most_repetitive)
print("Frequency:", max_count)


'''
Output

Most repetitive element: 2
Frequency: 3

'''
