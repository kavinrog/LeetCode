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

def test_find_kth_smallest():
    # Small-scale test
    arrays = [
        [1, 2, 3, 8],
        [2, 4, 6],
        [9, 19]
    ]
    k = 5
    assert find_kth_smallest(arrays, k) == 4, "Test Case 1 Failed"

    # Larger test (M = 999 arrays)
    M = 999
    arrays_large = []
    total_numbers = []
    for _ in range(M):
        size = random.randint(1, 20)
        arr = sorted(random.randint(1, 1000) for _ in range(size))
        arrays_large.append(arr)
        total_numbers.extend(arr)

    total_numbers.sort()
    k_large = 5000  # Kth position

    expected = total_numbers[k_large - 1] if k_large <= len(total_numbers) else None
    result = find_kth_smallest(arrays_large, k_large)

    assert result == expected, "Large Test Case Failed"

    # Edge case: K greater than total elements
    assert find_kth_smallest([[1,2,3]], 10) == None, "Edge Case Test Failed"

    print("All tests passed successfully.")


# Run test
test_find_kth_smallest()
