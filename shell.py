def shell_sort(li):
    n = len(li)
    h = 1
    while h < n / 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and li[j-h] > li[j]:
                li[j], li[j-h] = li[j-h], li[j]
                j -= h
        h = int(h / 3)
    return li