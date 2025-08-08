from itertools import combinations

# Example list of 200 numbers
numbers = list(range(200))

# Generate all possible pairs from the list of numbers
all_pairs = list(combinations(numbers, 2))

# Generate all possible combinations of 4 pairs
all_combinations_of_4_pairs = list(combinations(all_pairs, 4))

# Print the number of combinations
print(len(all_combinations_of_4_pairs))

# Optionally, print the first few combinations of 4 pairs
for combination in all_combinations_of_4_pairs[:10]:
    print(combination)
