def solution(num):
    # 주어진 수가 1이면 0 반환
    if num == 1:
        return 0
    
    # 작업 횟수를 세는 변수
    count = 0
    
    # 1이 될 때까지 반복
    while num != 1:
        # 500번 넘게 반복하면 -1 반환
        if count >= 500:
            return -1
        
        # 짝수라면 2로 나누기
        if num % 2 == 0:
            num = num // 2
        # 홀수라면 3을 곱하고 1 더하기
        else:
            num = num * 3 + 1
            
        # 작업 횟수 증가
        count += 1
    
    return count