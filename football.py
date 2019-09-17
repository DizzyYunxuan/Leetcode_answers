def merge(intervals):
    if not intervals:
        return 
    intervals.sort()
    res, t = [], intervals[0].copy()
    for i in range(1, len(intervals)):
        if intervals[i][0] > t[1]:
            res.append(t)
            t = intervals[i]
        else:
            t[1] = max(intervals[i][1], t[1])     
    res.append(t)  
    return res

def check(balls, intervals):
    res = 0
    for ball in balls:
        for inter in intervals:
            if ball >= inter[0]:
                if ball <= inter[1]:
                    res += 1
    return res

if __name__ == "__main__":
    m, n = map(int, input().split())
    intervals, balls = [], []
    for _ in range(m):
        intervals.append(list(map(int, input().split())))
    for _ in range(n):
        balls.append(int(input()))
    if not balls or not intervals:
        res = 0
    intervals = merge(intervals)
    res = check(balls, intervals)
