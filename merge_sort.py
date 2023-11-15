 # O(n) to merge two sorted lists into a sorted list
def merge_sorted_lists(list1, list2):
    index1 = 0
    index2 = 0
    merged_list = []
    # Collect the font value while both lists are not empty
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1
    # Add remaining values
    merged_list += list1[index1:]
    merged_list += list2[index2:]
    return merged_list

# test 1
merged_lists = merge_sorted_lists([2, 4, 7, 8], [1, 3, 5, 6])
print(merged_lists)

# test 2
merged_lists = merge_sorted_lists([1, 2, 3, 4], [5, 6, 7, 8])
print(merged_lists)

# split the list in half, sort both recursively and then use the merge_sorted_lists() function to merge the two sorted lists
def merge_sort(values):
    # Base case
    # the base case is when either the list becomes empty or it contains a single element. In both of these cases, the list is sorted
    if len(values) < 2:
        return values
    # General case
    midpoint = len(values) // 2
    sorted_first_half = merge_sort(values[:midpoint])
    sorted_second_half = merge_sort(values[midpoint:])
    return merge_sorted_lists(sorted_first_half, sorted_second_half)

merge_sort([2, 4, 7, 8, 1, 3, 5, 6])

# The number of levels, h, is equal to the number of times we need to cut the list in half to reach a list with a single element (or empty).
# We've learned that this is O(log(n)). We conclude that the time complexity of merge_sort() is O(n × log(n)).
