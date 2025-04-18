from collections import deque
def maxslidewindow(nums, k):
    q = deque()
    res = []
    
    for i in range(len(nums)):
        while q and q[0] < i - k + 1:
            q.popleft()
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k-1:
            res.append(nums[q[0]])
    return res 
            
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxslidewindow(nums, k))