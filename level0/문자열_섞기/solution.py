def solution(str1, str2):
    result = ''
    
    for a, b in zip(str1, str2):
        result += a + b
        
    return result