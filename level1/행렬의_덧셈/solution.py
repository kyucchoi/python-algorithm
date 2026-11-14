# 방법 1
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []
    
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])

        answer.append(row)
        
    return answer

# zip 함수 사용
def solution(arr1, arr2):
    answer = []

    for row1, row2 in zip(arr1, arr2):
        row = []

        for a, b in zip(row1, row2):
            row.append(a + b)

        answer.append(row)
        
    return answer