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