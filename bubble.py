def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j] >= li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li