def solution(numbers, n):
    sum = 0
    
    for num in numbers:
        sum += num      # 현재 숫자를 더함
        
        if sum > n:     # 합이 n보다 커지면
            break       # 반복문 종료
            
    return sum