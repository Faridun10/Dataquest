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
        
merged_lists = merge_sorted_lists([1, 2, 3, 4], [5, 6, 7, 8])
print(merged_lists)

def merge_sort(values):
    # Base case
    if len(values) < 2:
        return values
    # General case
    midpoint = len(values) // 2
    sorted_first_half = merge_sort(values[:midpoint])
    sorted_second_half = merge_sort(values[midpoint:])
    return merge_sorted_lists(sorted_first_half, sorted_second_half)

merge_sort([2, 4, 7, 8, 1, 3, 5, 6])
