def maxProductArray(arr):
    curr_max = arr[0]
    curr_min = arr[0]
    global_max =arr[0]
    
    for i in range(1, len(arr)):
        temp = curr_max
        curr_max = max(arr[i], arr[i] * curr_max, arr[i] * curr_min)
        curr_min = min(arr[i], arr[i] * temp, arr[i] * curr_min)
        global_max = max(global_max, curr_max)
    return global_max
        