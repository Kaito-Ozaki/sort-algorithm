import copy
import random

from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from shell import shell_sort

# 元データ生成
data_len = 100
unsorted = random.sample(range(-100, 100), data_len)

# バブルソート実行
print("======= bubble =======")
unsorted_for_bubble = copy.deepcopy(unsorted)
print(unsorted_for_bubble)
print("==============")
sorted_by_bubble = bubble_sort(unsorted_for_bubble)
print(sorted_by_bubble)
print("======= bubble =======")

# 選択ソート実行
print("======= selection =======")
unsorted_for_selection = copy.deepcopy(unsorted)
print(unsorted_for_selection)
print("==============")
sorted_by_selection = selection_sort(unsorted_for_selection)
print(sorted_by_selection)
print("======= selection =======")

# 挿入ソート実行
print("======= insertion =======")
unsorted_for_insertion = copy.deepcopy(unsorted)
print(unsorted_for_insertion)
print("==============")
sorted_by_insertion = insertion_sort(unsorted_for_insertion)
print(sorted_by_insertion)
print("======= insertion =======")

# シェルソート実行
print("======= shell =======")
unsorted_for_shell = copy.deepcopy(unsorted)
print(unsorted_for_shell)
print("==============")
sorted_by_shell = shell_sort(unsorted_for_shell)
print(sorted_by_shell)
print("======= shell =======")