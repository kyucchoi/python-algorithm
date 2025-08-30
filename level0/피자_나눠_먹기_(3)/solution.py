# 방법 1
def solution(slice, n):
    return ((n - 1) // slice) + 1

# 방법 2
def solution(slice, n):
    pizza = 0
    answer = 0
    
    while pizza < n:
        pizza += slice
        answer += 1
            
    return answer