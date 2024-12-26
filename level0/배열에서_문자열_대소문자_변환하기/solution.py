def solution(strArr):
    result = []
    
    for i, s in enumerate(strArr):
        if i % 2 == 0:  # 짝수 인덱스
            result.append(s.lower())
        else:           # 홀수 인덱스
            result.append(s.upper())
            
    return result