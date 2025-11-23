def solution(arr):
    stk = []
    
    for num in arr:
        # stk이 비어있으면 현재 숫자 추가
        if not stk:
            stk.append(num)
        elif stk[-1] == num:
            stk.pop()
        elif stk[-1] != num:
            stk.append(num)
    
    # 빈 배열이면 [-1] 반환
    return stk if stk else [-1]