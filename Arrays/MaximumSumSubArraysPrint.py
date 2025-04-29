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

# Test the function
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    print(maxSumSubarrayPrint(arr, n))  # Output: 6
    arr = [1]
    n = len(arr)
    print(maxSumSubarrayPrint(arr, n))  # Output: 1
    arr = [5, 4, -1, 7, 8]
    n = len(arr)
    print(maxSumSubarrayPrint(arr, n))  # Output: 23
