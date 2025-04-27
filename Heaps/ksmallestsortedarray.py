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

