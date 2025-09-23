# 방법 1
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sliced = array[i - 1:j]
        sliced.sort()
        answer.append(sliced[k - 1])
        
    return answer

# 방법 2
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sliced = array[i - 1:j]
        sorted_arr = sorted(sliced)
        answer.append(sorted_arr[k - 1])
    
    return answer

# 방법 3
def solution(array, commands):
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]