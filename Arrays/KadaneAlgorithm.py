def maxSumSubArray(arr):
    # Using Kadane's algorithm to find the maximum sum of a contiguous subarray
    global_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        global_sum = max(global_sum ,curr_sum)
    return global_sum

