def selection_sort(lst):
    n = len(lst)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i] 
    return lst