def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    if left_i < len(left):
        merged.extend(left[left_i:])
    if right_i < len(right):
        merged.extend(right[right_i:])
    
    return merged