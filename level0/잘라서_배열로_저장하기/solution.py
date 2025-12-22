def solution(my_str, n):
    result = []
    
    for i in range(0, len(my_str), n):
        chunk = my_str[i:i + n]
        result.append(chunk)
    
    return result