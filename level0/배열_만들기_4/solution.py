def solution(arr):
    stk = []  # 빈 배열로 시작
    i = 0     # 인덱스 초기화
    
    while i < len(arr):  # i가 arr의 길이보다 작은 동안 반복
        # stk가 비어있으면 현재 값 추가
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        # stk의 마지막 값이 현재 값보다 작으면 현재 값 추가
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        # stk의 마지막 값이 현재 값보다 크거나 같으면 마지막 값 제거
        else:
            stk.pop()
            
    return stk