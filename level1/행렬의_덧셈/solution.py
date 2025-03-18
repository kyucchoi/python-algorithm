# 방법 1
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

def solution(arr1, arr2):
    result = []
    
    # 바깥쪽 반복문: 행(row)을 처리
    for i in range(len(arr1)):
        row_result = []
        
        # 안쪽 반복문: 각 행의 열(column)을 처리
        for j in range(len(arr1[0])):
            # arr1과 arr2의 동일한 위치(i행 j열)의 원소를 더함
            sum_value = arr1[i][j] + arr2[i][j]
            row_result.append(sum_value)
        
        # 완성된 행을 결과 행렬에 추가
        result.append(row_result)
    
    return result