# 방법 1
def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        stack = []

        for j in range(n):
            c = s[(i + j) % n]

            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    break
                if ((c == ')' and stack[-1] == '(') or
                    (c == ']' and stack[-1] == '[') or
                    (c == '}' and stack[-1] == '{')):
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1

    return answer

# 방법 2
def solution(s):
    def is_valid(string):
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in string:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack[-1]] != char:
                    return False
                
                stack.pop()
        
        return len(stack) == 0
    
    answer = 0

    for x in range(len(s)):
        rotated = s[x:] + s[:x]

        if is_valid(rotated):
            answer += 1
    
    return answer