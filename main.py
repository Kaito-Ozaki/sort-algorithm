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
data_len = 100000
unsorted = random.sample(range(-100000, 100000), data_len)
print(unsorted)

# バブルソート実行
print("======= bubble =======")
unsorted_for_bubble = copy.deepcopy(unsorted)
start = time.time()
sorted_by_bubble = bubble_sort(unsorted_for_bubble)
print("{} sec".format(time.time() - start))
print(sorted_by_bubble)
print("======= bubble =======")

# 選択ソート実行
print("======= selection =======")
unsorted_for_selection = copy.deepcopy(unsorted)
start = time.time()
sorted_by_selection = selection_sort(unsorted_for_selection)
print("{} sec".format(time.time() - start))
print(sorted_by_selection)
print("======= selection =======")

# 挿入ソート実行
print("======= insertion =======")
unsorted_for_insertion = copy.deepcopy(unsorted)
start = time.time()
sorted_by_insertion = insertion_sort(unsorted_for_insertion)
print("{} sec".format(time.time() - start))
print(sorted_by_insertion)
print("======= insertion =======")

# シェルソート実行
print("======= shell =======")
unsorted_for_shell = copy.deepcopy(unsorted)
start = time.time()
sorted_by_shell = shell_sort(unsorted_for_shell)
print("{} sec".format(time.time() - start))
print(sorted_by_shell)
print("======= shell =======")

# クイックソート実行
print("======= quick =======")
unsorted_for_quick = copy.deepcopy(unsorted)
start = time.time()
sorted_by_quick = quick_sort(unsorted_for_quick)
print("{} sec".format(time.time() - start))
print(sorted_by_quick)
print("======= quick =======")

# ヒープソート実行
print("======= heap =======")
unsorted_for_heap = copy.deepcopy(unsorted)
start = time.time()
sorted_by_heap = heap_sort(unsorted_for_heap)
print("{} sec".format(time.time() - start))
print(sorted_by_heap)
print("======= heap =======")

# マージソート実行
print("======= merge =======")
unsorted_for_merge = copy.deepcopy(unsorted)
start = time.time()
sorted_by_merge = merge_sort(unsorted_for_merge)
print("{} sec".format(time.time() - start))
print(sorted_by_merge)
print("======= merge =======")