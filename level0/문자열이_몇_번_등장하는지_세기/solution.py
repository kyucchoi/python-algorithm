def solution(myString, pat):
    count = 0
    
    # 가능한 모든 위치에서 pat 확인
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat:
            count += 1
            
    return count