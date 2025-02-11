def solution(arr, flag):
    X = []  # 빈 배열로 시작
    
    # arr와 flag를 동시에 순회
    for i in range(len(arr)):
        if flag[i]:
            # True인 경우: arr[i]를 arr[i] * 2번 추가
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            # False인 경우: 마지막 arr[i]개의 원소 제거
            X = X[:-arr[i]]
    
    return X