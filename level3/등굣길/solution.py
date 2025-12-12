def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    
    for x, y in puddles:
        dp[y][x] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if i == 1 and j == 1:
                continue
            
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            
            # 위에서 오는 경로
            if dp[i - 1][j] > 0:
                dp[i][j] += dp[i - 1][j]
            
            # 왼쪽에서 오는 경로
            if dp[i][j - 1] > 0:
                dp[i][j] += dp[i][j - 1]
            
            dp[i][j] %= 1000000007
    
    return dp[n][m]