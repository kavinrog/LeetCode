import heapq
def findkSmallestNumbers(nums, k):
    """
    Find the k smallest numbers in an array.
    :param nums: List[int] - The input array
    :param k: int - The number of smallest elements to find
    :return: List[int] - The k smallest numbers in the array
    """
    if not nums or k <= 0:
        return []
    maxHeap = []
    
    for num in nums:
        heapq.heappush(maxHeap, -num)
        if(len(maxHeap)>k):
            maxHeap.pop()
    return -maxHeap[0]

    