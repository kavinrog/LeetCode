def maxSumSubArray(arr):
    # Using Kadane's algorithm to find the maximum sum of a contiguous subarray
    global_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        global_sum = max(global_sum ,curr_sum)
    return global_sum

# Test the function
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSumSubArray(arr))  # Output: 6
    arr = [1]
    print(maxSumSubArray(arr))  # Output: 1
    arr = [5,4,-1,7,8]
    print(maxSumSubArray(arr))  # Output: 23