import heapq
def kLargestNumber(nums, k):
    """
    This function returns the k largest numbers from the given list of numbers.
    
    :param nums: List of integers
    :param k: Integer representing the number of largest elements to return
    :return: List of the k largest integers
    """
    if not nums or k <=0:
        return []
    
    minHeap =[]
    for num in nums:
        heapq.heappush(minHeap, num)
        if(len(minHeap)>k):
            heapq.heappop(minHeap)
    return minHeap[0]
    
