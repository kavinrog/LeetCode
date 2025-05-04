import heapq
def findkSmallestNumbers(nums, k, return_k_smallest_list=1):
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
            heapq.heappop(maxHeap)
    print(maxHeap)
    if(return_k_smallest_list == 1):
        return sorted([-x for x in maxHeap])
    else:   
        return -maxHeap[0]

# Test the function
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findkSmallestNumbers(nums, k))  # Output: [1, 2]
    
    nums = [3, 2, 3]
    k = 2
    print(findkSmallestNumbers(nums, k))  # Output: [2, 3]
    
    nums = [1]
    k = 1
    print(findkSmallestNumbers(nums, k))  # Output: [1]

    