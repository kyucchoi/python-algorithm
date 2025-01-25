def solution(strArr):
    result = []
    
    for s in strArr:
        # "ad"가 없는 문자열만 추가
        if "ad" not in s:
            result.append(s)
            
    return result