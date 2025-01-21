def solution(myString, pat):
    # 대소문자 구분하지 않도록 모두 소문자로 변환
    myString = myString.lower()
    pat = pat.lower()
    
    # 문자열 길이
    myString_len = len(myString)
    pat_len = len(pat)
    
    # pat의 길이가 더 길면 불가능
    if pat_len > myString_len:
        return 0
        
    # 모든 가능한 부분 문자열 확인
    for i in range(myString_len - pat_len + 1):
        if myString[i:i + pat_len] == pat:
            return 1
            
    return 0