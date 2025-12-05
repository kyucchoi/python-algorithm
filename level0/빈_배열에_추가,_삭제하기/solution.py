def solution(arr, flag):
    X = []
    
    for i in range(len(arr)):
        if flag[i]:
            # True인 경우: arr[i]를 arr[i] * 2번 추가
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            # False인 경우: 마지막 arr[i]개의 원소 제거
            X = X[:-arr[i]]
    
    return X