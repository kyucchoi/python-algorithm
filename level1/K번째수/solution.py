# 방법 1
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        # 배열 자르기 (i - 1부터 j까지)
        sliced = array[i - 1:j]
        # 정렬
        sliced.sort()
        # k번째 수 추가
        answer.append(sliced[k - 1])
        
    return answer

# 방법 2
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:  # commands의 각 요소를 직접 i, j, k로 언패킹
        sliced = array[i - 1:j]

        sorted_arr = sorted(sliced)

        answer.append(sorted_arr[k - 1])
    
    return answer

# 방법 3
def solution(array, commands):
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]