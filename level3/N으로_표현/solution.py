def solution(N, number):
    if N == number:
        return 1
    
    # dp[i] = N을 i개 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]  # dp[0]은 사용 안 함
    
    for i in range(1, 9):
        # 1. N을 i개 연속으로 붙인 수 (예: 55, 555)
        dp[i].add(int(str(N) * i))
        
        # 2. 두 그룹으로 나누어 사칙연산
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)

                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        if number in dp[i]:
            return i
    
    return -1