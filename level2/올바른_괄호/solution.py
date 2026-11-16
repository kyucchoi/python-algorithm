# 개수 세기 방법
def solution(s):
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
            
    return count == 0

# 스택 풀이 방법
def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False

            stack.pop()

    return not stack