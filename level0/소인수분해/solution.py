def solution(n):
    answer = []
    divisor = 2
    
    while divisor <= n:
        if n % divisor == 0:
            if divisor not in answer:
                answer.append(divisor)
                
            n //= divisor
        else:
            divisor += 1
        
    return answer