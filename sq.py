def solution(n, nums):
    nums = sorted(nums, reverse=True)
    i = 0
    l = []
    s = 0

    while i < len(nums):
        if abs(nums[i] - nums[i-1]) <= 1:
            l.append(nums[i])
            i += 2
            break
    while i < len(nums):
        if abs(nums[i] - nums[i-1]) <= 1:
            l2 = nums[i]
            i += 2
            break
    
         