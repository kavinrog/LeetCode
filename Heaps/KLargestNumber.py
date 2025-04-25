import heapq

RETURN_K_LARGEST_LIST = 1

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
    if(RETURN_K_LARGEST_LIST == 1):
        return sorted(minHeap, reverse=True)
    else:
        return minHeap[0]

    
# Test the function
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(kLargestNumber(nums, k))  # Output: [5, 6]
    
    nums = [3, 2, 3]
    k = 2
    print(kLargestNumber(nums, k))  # Output: [3, 3]
    
    nums = [1]
    k = 1
    print(kLargestNumber(nums, k))  # Output: [1]