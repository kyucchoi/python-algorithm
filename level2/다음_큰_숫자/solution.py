def solution(n):
    # n의 2진수에서 1의 개수
    one_count = bin(n).count('1')
    
    # n + 1부터 검사
    num = n + 1
    
    # 조건 만족하는 수 찾기
    while bin(num).count('1') != one_count:
        num += 1
        
    return num