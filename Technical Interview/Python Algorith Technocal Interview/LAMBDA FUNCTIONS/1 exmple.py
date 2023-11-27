# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(add(2, 3))          # Output: 5
print(add_lambda(2, 3))    # Output: 5


# Using a regular function with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]

pairs = [(1, 5), (2, 3), (4, 1), (3, 2)]

# Sorting by the second element of each tuple
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(4, 1), (3, 2), (2, 3), (1, 5)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using filter() with a lambda function to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8]
# Finding the maximum length string in a list
words = ["apple", "banana", "kiwi", "strawberry"]

max_length_word = max(words, key=lambda x: len(x))

print(max_length_word)  # Output: "strawberry"
