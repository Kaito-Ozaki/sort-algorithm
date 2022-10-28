def shell_sort(lst):
    n = len(lst)
    h = 1
    while h < n / 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and lst[j-h] > lst[j]:
                lst[j], lst[j-h] = lst[j-h], lst[j]
                j -= h
        h = h // 3
    return lst