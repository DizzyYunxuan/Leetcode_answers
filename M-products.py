def solution(M, l_m):
    l_m.sort()
    s_half = sum(l_m) // 2
    dp = [0 for _ in range(M+1)]

    for i in range(1, M+1):
        dp[i] = dp[i-1]
        if dp[i-1] + l_m[i-1] <= s_half:
            dp[i] = dp[i-1] + l_m[i-1]
            continue
        else:
            for j in range(i-1):
                if dp[i-1] - l_m[j] + l_m[i-1] <= s_half:
                    dp[i] = max(dp[i-1] - l_m[j] + l_m[i-1], dp[i])
    return max(dp[-1], sum(l_m)-dp[-1])


if __name__ == "__main__":
    M = int(input())
    l_m = input().split()
    l_m = list(map(lambda x: int(x), l_m))
    print(solution(M, l_m))