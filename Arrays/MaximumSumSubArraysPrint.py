def maxSumSubarrayPrint(arr, n):
    curr_sum = arr[0]
    global_sum = arr[0]
    start = 0 
    end = 0 
    temp_start = 0 
    
    for i in range(1, n):
        curr_sum += arr[i]
        
        if arr[i] > curr_sum:
            curr_sum = arr[i]
            temp_start = i
        if curr_sum > global_sum:
            global_sum = curr_sum
            start = temp_start
            end = i 
    print("Maximum sum subarray is:", arr[start:end+1])
    print("Maximum sum is:", global_sum)
    return global_sum
