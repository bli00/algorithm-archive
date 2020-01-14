def videoStitching(clips: List[List[int]], T: int) -> int:
    # sort the clips in ascending order according to starting point
    clips.sort(key=lambda x: x[0])
    
    i, count = 0, 0
    curEnd, curMax = 0, 0
    while i < len(clips) and curEnd < T:
        # if there is a gap amongst the sorted clips
        if clips[i][0] > curEnd: return -1
        
        # sweep across the current interval and find the next ending point,
        # which will create the next interval.
        while i < len(clips) and clips[i][0] <= curEnd:
            curMax = max(clips[i][1], curMax)
            i += 1
        
        curEnd = curMax
        count += 1
    
    # check if the clips can reach the end
    return count if curEnd >= T else -1
    