def solution(n):
    # 약수들의 합을 저장할 변수
    total = 0
    
    # 1부터 n까지 반복
    for i in range(1, n + 1):
        # i가 n의 약수인지 확인
        if n % i == 0:
            total += i
            
    return total