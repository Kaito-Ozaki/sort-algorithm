import random

from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort

# 元データ生成
data_len = 100
unsorted = random.sample(range(-100, 100), data_len)
print(unsorted)

# バブルソート
print("==============")
sorted_by_bubble = bubble_sort(unsorted)
print(sorted_by_bubble)

# 選択ソート
print("==============")
sorted_by_selection = selection_sort(unsorted)
print(sorted_by_selection)

# 挿入ソート
print("==============")
sorted_by_insertion = insertion_sort(unsorted)
print(sorted_by_insertion)