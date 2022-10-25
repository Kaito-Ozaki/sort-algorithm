import random

from bubble import bubble_sort
from selection import selection_sort

# 元データ生成
data_len = 100
unsorted = random.sample(range(-100, 100), data_len)
print(unsorted)

# バブルソートでソートする
print("==============")
sorted_by_bubble = bubble_sort(unsorted)
print(sorted_by_bubble)

# 選択でソートする
print("==============")
sorted_by_selection = selection_sort(unsorted)
print(sorted_by_selection)