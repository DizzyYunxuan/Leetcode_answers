def solution(goodsnums, goodsdelta, N):
    # d = []
    # for i in range(len(goodsnums)):
    #     if goodsnums[i] <= N:
    #         d.append((goodsnums[i], goodsdelta[i]))
    # d.sort()
    d = list(zip(goodsnums, goodsdelta))
    dp = [[0] * (len(goodsnums)+1) for _ in range(len(goodsdelta)+1)]
    for i in range(1, len(goodsnums)+1):
        bag = 0
        for j in range(1, len(goodsdelta)+1):
            bag += d[j-1][0]
            bag = min(bag, N)
            if goodsnums[i-1] > bag:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], d[i-1][0]*d[i-1][1]+dp[i-1][j-1])
    return '%.4f' % dp[-1][-1]

if __name__ == "__main__":
    goodsnums, goodsdelta = [100,320,120,20,80], [-0.05, 0.05, 0, 0.03, 0.04]
    res = solution(goodsnums, goodsdelta, 500)
    x = 1
