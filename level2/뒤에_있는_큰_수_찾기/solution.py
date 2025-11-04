def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에서 인덱스를 꺼내어 해당 위치의 뒷 큰수를 현재 숫자로 설정
            answer[stack.pop()] = numbers[i]
        
        stack.append(i)
    
    return answer