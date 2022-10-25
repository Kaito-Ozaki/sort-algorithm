def selection_sort(li):
    n = len(li)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if li[j] < li[min]:
                min = j
        li[i], li[min] = li[min], li[i] 
    return li