def solution(numbers, n):
    answer = 0
    
    for num in numbers:
        answer += num      # 현재 숫자를 더함
        
        if answer > n:     # 합이 n보다 커지면
            break       # 반복문 종료
            
    return answer