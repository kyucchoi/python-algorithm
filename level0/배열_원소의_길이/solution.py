# 방법 1
def solution(strlist):
    answer = []
    
    for char in strlist:
        answer.append(len(char))
        
    return answer

# 방법 2
def solution(strlist):
    return list(map(len, strlist))