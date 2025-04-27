import heapq
def ksmallestsortedarray(arrays, k):
    heap = []
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))
            
    count = 0 
    while heap:
        val, arr_idx, ele_idx = heapq.heappop(heap)
        count +=1
        if count == k:
            return val
        if ele_idx +1 < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][ele_idx +1],arr_idx, ele_idx +1))
    return -1 

# Test the function
if __name__ == "__main__":
    arrays = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    k = 5
    print(ksmallestsortedarray(arrays, k))  # Output: 5
    
    arrays = [[1, 2], [3, 4], [5, 6]]
    k = 4
    print(ksmallestsortedarray(arrays, k))  # Output: 4
    
    arrays = [[1], [2], [3]]
    k = 2
    print(ksmallestsortedarray(arrays, k))  # Output: 2