def minmeetingroom(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])
    res = count = 0 
    s = e = 0 
    while s < len(intervals):
        if start[s] < end[e]:
            count+=1
            s+=1
        else:
            e+=1
            count-=1
        res = max(count, res)
    return res 
    