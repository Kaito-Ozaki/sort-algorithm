def heap_sort(lst):
    n = len(lst)
    for i in range(n//2-1, -1, -1):
        heapify(lst, i, n)

    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
        
    return lst

def heapify(lst, i, heap_size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and lst[left] > lst[largest]:
        largest = left

    if right < heap_size and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, largest, heap_size)