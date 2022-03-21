# Sets
# They are the basics of sets I'll dive into them later.

# Set is a collection data type that is
# - iterable
# - mutable
# - has no duplicate  elements

numbers = [1,1,14,3,5,5]
first = set(numbers)
second = {1,2,3,4,5}

# union
print(first | second)

# intersection
print(first & second)

# difference
print(first - second)

# symmetric difference
print(first ^ second)

# Sets does not support indexing