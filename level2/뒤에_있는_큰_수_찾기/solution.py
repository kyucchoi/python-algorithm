def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        # 현재 숫자가 스택에 있는 숫자들의 뒷 큰수인지 확인
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        
        stack.append(i)
    
    return answer