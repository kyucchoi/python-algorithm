def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 결과 배열을 -1로 초기화
    stack = []  # 인덱스를 저장할 스택
    
    for i in range(n):
        # 현재 숫자가 스택에 있는 인덱스들의 숫자보다 클 때
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에서 인덱스를 꺼내어 해당 위치의 뒷 큰수를 현재 숫자로 설정
            answer[stack.pop()] = numbers[i]
        
        # 현재 인덱스를 스택에 추가
        stack.append(i)
    
    return answer