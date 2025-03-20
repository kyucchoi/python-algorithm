# 방법 1
def solution(t, p):
    count = 0
    p_len = len(p)
    p_value = int(p)
    
    # t의 부분문자열 추출 및 비교
    for i in range(len(t) - p_len + 1):
        substring = t[i:i + p_len]

        if int(substring) <= p_value:
            count += 1
    
    return count

# 내 방법
def solution(t, p):
    count = 0
    p_len = len(p)
    p_value = int(p)
    
    # 유효한 범위까지만 반복 (부분문자열의 길이가 p와 같도록)
    for n in range(len(t) - p_len + 1):
        # 부분문자열을 정수로 변환하여 비교
        if int(t[n:n + p_len]) <= p_value:
            count += 1
            
    return count