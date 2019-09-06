def best(v, valueSum, left, right):
    if right - left > 1:
        leftsum = valueSum - best(v, valueSum-v[left], left+1, right)
        rightsum = valueSum - best(v, valueSum-v[right], left, right-1)
        return 'Yes' if leftsum > rightsum else 'No'
    elif left != right:
        return 'Yes' if v[left] > v[right] else 'No'
    return 'Yes'

def maxValue(v, length):
    valueSum = 0
    for i in range(length):
        valueSum += v[i]
    return best(v, valueSum, 0, length - 1)

if __name__ == "__main__":
    res = maxValue([1,2,3,6,9,5,7,4,2,6,9,5,8,7,2,1,55,3,6,9,7,5,2], 23)
    print(res)

        