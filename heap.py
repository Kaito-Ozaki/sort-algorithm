def heap_sort(li):
    n = len(li)
    for i in range(n//2-1, -1, -1):
        heapify(li, i, n)

    for i in range(n-1, 0, -1):
        li[0], li[i] = li[i], li[0]
        heapify(li, 0, i)
        
    return li

def heapify(li, i, heap_size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and li[left] > li[largest]:
        largest = left

    if right < heap_size and li[right] > li[largest]:
        largest = right

    if largest != i:
        li[largest], li[i] = li[i], li[largest]
        heapify(li, largest, heap_size)