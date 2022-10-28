def quick_sort(li):
    if len(li) <= 1:
        return li

    pivot = li[0]
    l = []
    c = []
    r = []

    for v in li:
        if v < pivot:
            l.append(v)
        elif v > pivot:
            r.append(v)
        else:
            c.append(v)
    
    l = quick_sort(l)
    r = quick_sort(r)

    return l + c + r