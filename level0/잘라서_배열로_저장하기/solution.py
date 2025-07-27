def solution(my_str, n):
    result = []
    
    # n개씩 잘라서 배열에 저장
    for i in range(0, len(my_str), n):
        chunk = my_str[i:i + n]
        result.append(chunk)
    
    return result