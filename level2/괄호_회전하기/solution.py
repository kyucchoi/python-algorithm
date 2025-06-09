# 방법 1
def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        stack = []

        for j in range(n):
            c = s[(i + j) % n]

            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    break
                if ((c == ")" and stack[-1] == "(") or
                    (c == "]" and stack[-1] == "[") or
                    (c == "}" and stack[-1] == "{")):
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1

    return answer

# 방법 2
def solution(s):
    # 조기 종료 조건들
    if len(s) % 2 == 1:  # 홀수 길이는 불가능
        return 0
    
    # 각 괄호 종류별 개수가 맞지 않으면 불가능
    if (s.count('(') != s.count(')') or 
        s.count('[') != s.count(']') or 
        s.count('{') != s.count('}')):
        return 0
    
    def is_valid_brackets(string):
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in string:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()] != char:
                    return False
                
        return len(stack) == 0
    
    count = 0

    for x in range(len(s)):
        rotated = s[x:] + s[:x]

        if is_valid_brackets(rotated):
            count += 1

    return count