def solution(ingredient):
    stack = []  # 재료를 쌓아둘 스택
    count = 0   # 완성된 햄버거 개수
    
    for item in ingredient:
        stack.append(item)  # 재료 추가
        
        # 스택의 길이가 4 이상이고 마지막 4개 재료가 햄버거 순서(1-2-3-1)와 일치하는지 확인
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 완성! 마지막 4개 재료 제거
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            count += 1  # 햄버거 개수 증가
    
    return count