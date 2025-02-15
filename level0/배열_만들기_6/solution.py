def solution(arr):
    stk = []  # 빈 스택으로 시작
    
    for num in arr:
        # stk이 비어있으면 현재 숫자 추가
        if not stk:
            stk.append(num)
        # stk의 마지막 원소가 현재 숫자와 같으면 제거
        elif stk[-1] == num:
            stk.pop()
        # stk의 마지막 원소가 현재 숫자와 다르면 추가
        else:
            stk.append(num)
    
    # 빈 배열이면 [-1] 반환
    return stk if stk else [-1]