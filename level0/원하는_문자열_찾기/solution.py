def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    myString_len = len(myString)
    pat_len = len(pat)
    
    if pat_len > myString_len:
        return 0
        
    for i in range(myString_len - pat_len + 1):
        if myString[i:i + pat_len] == pat:
            return 1
            
    return 0