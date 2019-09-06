def solution(n, k, nums):
    s, count = 0, 0
    for i in range(len(nums)):
        s += min(nums[i], 8)
        if i+1 < len(nums):
            nums[i+1] += nums[i] - min(nums[i], 8)
        count += 1
        if count == n:
            break
    if s >= k:
        return count
    else:
        return -1

if __name__ == "__main__":
    n, k = 1, 9
    a = [10]
    res = solution(n,k, a)
    print(res)
