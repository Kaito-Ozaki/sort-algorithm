def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    left = []
    center = []
    right = []

    for v in lst:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            center.append(v)
    
    left = quick_sort(left)
    right = quick_sort(right)

    return left + center + right