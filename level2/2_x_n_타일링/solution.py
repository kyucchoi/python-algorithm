def solution(n):
    MOD = 1000000007
    
    if n <= 2:
        return n
    
    # 이전 2개 값만 저장 (공간 최적화)
    prev1, prev2 = 1, 2  # dp[1], dp[2]
    
    for i in range(3, n + 1):
        current = (prev1 + prev2) % MOD
        prev1, prev2 = prev2, current
    
    return prev2