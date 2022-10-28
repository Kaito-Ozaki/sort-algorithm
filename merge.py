def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    l = li[:mid]
    r = li[mid:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)

def merge(l, r):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(l) and r_i < len(r):
        if l[l_i] <= r[r_i]:
            merged.append(l[l_i])
            l_i += 1
        else:
            merged.append(r[r_i])
            r_i += 1

    if l_i < len(l):
        merged.extend(l[l_i:])
    if r_i < len(r):
        merged.extend(r[r_i:])
    
    return merged