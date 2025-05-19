def solution(s):
    stack = []
    
    for char in s:
        # 스택이 비어있지 않고, 스택의 맨 위 문자와 현재 문자가 같으면
        if stack and stack[-1] == char:
            stack.pop()  # 짝을 이루므로 제거
        else:
            stack.append(char)  # 스택에 추가
    
    # 스택이 비어있으면 모든 문자가 제거된 것 (성공)
    return 1 if not stack else 0