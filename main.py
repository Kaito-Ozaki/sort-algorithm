import copy
import random
import time

from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from shell import shell_sort
from quick import quick_sort
from heap import heap_sort
from merge import merge_sort

# 元データ生成
data_len = 100
unsorted = random.sample(range(-100, 100), data_len)

# バブルソート実行
print("======= bubble =======")
unsorted_for_bubble = copy.deepcopy(unsorted)
print(unsorted_for_bubble)
print("==============")
start = time.time()
sorted_by_bubble = bubble_sort(unsorted_for_bubble)
print(sorted_by_bubble)
print("{} sec".format(time.time() - start))
print("======= bubble =======")

# 選択ソート実行
print("======= selection =======")
unsorted_for_selection = copy.deepcopy(unsorted)
print(unsorted_for_selection)
print("==============")
start = time.time()
sorted_by_selection = selection_sort(unsorted_for_selection)
print(sorted_by_selection)
print("{} sec".format(time.time() - start))
print("======= selection =======")

# 挿入ソート実行
print("======= insertion =======")
unsorted_for_insertion = copy.deepcopy(unsorted)
print(unsorted_for_insertion)
print("==============")
start = time.time()
sorted_by_insertion = insertion_sort(unsorted_for_insertion)
print(sorted_by_insertion)
print("{} sec".format(time.time() - start))
print("======= insertion =======")

# シェルソート実行
print("======= shell =======")
unsorted_for_shell = copy.deepcopy(unsorted)
print(unsorted_for_shell)
print("==============")
start = time.time()
sorted_by_shell = shell_sort(unsorted_for_shell)
print(sorted_by_shell)
print("{} sec".format(time.time() - start))
print("======= shell =======")

# クイックソート実行
print("======= quick =======")
unsorted_for_quick = copy.deepcopy(unsorted)
print(unsorted_for_quick)
print("==============")
start = time.time()
sorted_by_quick = quick_sort(unsorted_for_quick)
print(sorted_by_quick)
print("{} sec".format(time.time() - start))
print("======= quick =======")

# ヒープソート実行
print("======= heap =======")
unsorted_for_heap = copy.deepcopy(unsorted)
print(unsorted_for_heap)
print("==============")
start = time.time()
sorted_by_heap = heap_sort(unsorted_for_heap)
print(sorted_by_heap)
print("{} sec".format(time.time() - start))
print("======= heap =======")

# マージソート実行
print("======= merge =======")
unsorted_for_merge = copy.deepcopy(unsorted)
print(unsorted_for_merge)
print("==============")
start = time.time()
sorted_by_merge = merge_sort(unsorted_for_merge)
print(sorted_by_merge)
print("{} sec".format(time.time() - start))
print("======= merge =======")