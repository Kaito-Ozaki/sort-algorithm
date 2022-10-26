def insertion_sort(li):
    for i in range(1, len(li)):
        ins = i
        for j in range(0, i+1):
            if li[i] >= li[j]:
                ins = j
        li[i], li[ins] = li[ins], li[i]
    return li