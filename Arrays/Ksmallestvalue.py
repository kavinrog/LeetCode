import heapq
import random

def find_kth_smallest(arrays, k):
    min_heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    number_count = 0
    result = None
    while min_heap and number_count < k:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result = val
        number_count += 1

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

    if number_count == k:
        return result
    else:
        return None
