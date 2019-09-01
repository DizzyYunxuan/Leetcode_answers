def findAll(nums, cursum, res):
    if not nums:
        res.append(cursum)
        return 
    for i in range(len(nums)):
        findAll(nums[:i] + nums[i+1:], cursum+nums[i], res)
        findAll(nums[:i] + nums[i+1:], cursum-nums[i], res)
    return 
    
def Solution(length, steps):
    tmp = []
    findAll(steps, 0, tmp)
    tmp = set(tmp)
    allDestinationFromStart = []
    for i in tmp:
        if abs(i) >= length:
            continue
        else:
            allDestinationFromStart.append(i)
    res = [0] * length
    for i in range(length):
        for j in allDestinationFromStart:
            if i+j >= 0 and  i+j <= length-1:
                res[i] = 1
    return sum(res)

        

if __name__ == "__main__":
    res = []
    res = Solution(10,[5, 2, 6])