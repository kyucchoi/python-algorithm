def solution(n):
    if n % 2 == 1:
        result = 0
        
        for i in range(1, n + 1, 2):
            result += i
            
        return result
    else:
        result = 0
        
        for i in range(2, n + 1, 2):
            result += i*i
            
        return result
    
# def solution(n):
   # n이 홀수인 경우
   # if n % 2 == 1:
       # return sum(i for i in range(1, n+1, 2))
   # n이 짝수인 경우
   # else:
       # return sum(i*i for i in range(2, n+1, 2))