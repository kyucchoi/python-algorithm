def solution(n):
    # n의 제곱근 계산
    x = n**0.5
    
    # 제곱근이 정수인지 확인
    if x == int(x):
        # 정수라면 x+1의 제곱 반환
        return (int(x) + 1)**2
    else:
        # 정수가 아니라면 -1 반환
        return -1