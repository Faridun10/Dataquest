def recursive_sum(values):
    # Base case: the list is empty
    if not values:
        return 0
    # General case: the list is not empty
    return values[0] + recursive_sum(values[1:])

result = recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# recursive length function
fruits = ["apple", "orange", "pear", "fig", "passionfruit"]
def list_len(lst):
    if not lst:
        return 0
    return 1 + list_len(lst[1:])

num_fruits = list_len(fruits)
print(num_fruits)
