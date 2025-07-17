def solution(num_list, n):
    result = []
    
    # n개씩 묶어서 2차원 배열 만들기
    for i in range(0, len(num_list), n):
        row = num_list[i:i + n]
        result.append(row)
    
    return result