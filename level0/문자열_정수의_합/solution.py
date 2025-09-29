# 방법 1
def solution(num_str):
    answer = 0
    
    for num in num_str:
        answer += int(num)
        
    return answer

# 방법 2
def solution(num_str):
    return sum(map(int, list(num_str)))