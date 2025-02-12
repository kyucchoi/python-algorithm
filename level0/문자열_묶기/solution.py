def solution(strArr):
    # 길이별로 개수를 저장할 딕셔너리
    length_count = {}
    
    # 각 문자열의 길이를 카운트
    for s in strArr:
        length = len(s)
        length_count[length] = length_count.get(length, 0) + 1
    
    # 가장 큰 개수 반환
    return max(length_count.values())