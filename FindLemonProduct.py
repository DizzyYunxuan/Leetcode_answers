def lemon(A, B):
    quick_sort(A, 0, len(A)-1)
    quick_sort(B, 0, len(B)-1)
    Amin, Amax = A[0], A[-1]
    Bmin, Bmax = B[0], B[-1]

    if Amax <= 0:
        if Bmax <= 0:
            return A[1] * B[0]
        else:
            if Bmin >= 0:    
                return A[-2] * B[0]
            else:
                return A[1] * B[0]
    elif Amin >= 0:
        if Bmax <= 0:
            return A[1] * B[-1]
        else:
            return A[-2] * B[-1]
    else:
        if Bmax <= 0:
            return A[1] * B[0]
        else:
            if Bmin >= 0:    
                return A[-2] * B[-1]
            else:
                return max(A[1]*B[0], A[-2]*B[-1])

def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
    
def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i+1

# nums = [3,5,7,2,5,4,12,54,11]
# quick_sort(nums, 0, len(nums)-1)
# print(nums)

A, B = [-1, 0, 1,2,3], [-1, 0, 1]
# A, B = [20,18], [2,14]
print(lemon(A,B))
