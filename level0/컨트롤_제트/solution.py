def solution(s):
    tokens = s.split()
    
    stack = []
    
    for token in tokens:
        if token == "Z":
            # Z가 나오면 마지막 숫자를 제거
            if stack:
                stack.pop()
        else:
            stack.append(int(token))
    
    # 스택에 남은 숫자들의 합 반환
    return sum(stack)