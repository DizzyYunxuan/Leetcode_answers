def Solution(k, length, dp):
    for i in range(2, length[1]+1):
        

    # res = 0
    # for flowers in range(length[0], length[1]+1):
    #     maxpows = flowers // k     
    #     # for groupWhite in range(maxpows+1):
    #     #     if not groupWhite:
    #     #         res += 1
    #     #     else:
    #     #         res += flowers-groupWhite*k+1
        t = 1 + (flowers+1)*maxpows -(1+maxpows)*maxpows*k/2
    #     res += t

            
    return res

if __name__ == "__main__":
    length = [1,3]
    dp = [0 * length[1]-length[0]+1]
    dp[1] = 1
    res = Solution(2, length, dp)