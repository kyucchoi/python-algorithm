def solution(n):
    answer = 0
    
    for num in range(1, int(n**0.5) + 1):
        if num * num == n:
            answer += 1
        elif n % num == 0:
            answer += 2
    
    return answer