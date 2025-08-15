# 방법 1
def solution(s):
   count = 0  # 여는 괄호의 개수를 세는 변수
   
   for char in s:
       if char == '(':
           count += 1
       else:  # char == ')'
           count -= 1
       
       if count < 0:  # 닫는 괄호가 더 많은 경우
           return False
           
   return count == 0  # 모든 괄호가 짝이 맞으면 count는 0

# 방법 2
def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append('(')  # 여는 괄호를 스택에 추가
        elif char == ')':
            if not stack:  # 스택이 비어있는데 닫는 괄호가 나옴
                return False
            stack.pop()    # 여는 괄호와 짝 맞추기

    # 모든 괄호가 짝지어졌으면 스택이 비어있어야 함
    return len(stack) == 0