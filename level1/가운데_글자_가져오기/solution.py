def solution(s):
    # 문자열의 길이 계산
    length = len(s)
    
    # 길이가 홀수인 경우
    if length % 2 == 1:
        # 가운데 글자 반환 (인덱스는 0부터 시작하므로 길이의 절반을 내림)
        return s[length // 2]
    
    # 길이가 짝수인 경우
    else:
        # 가운데 두 글자 반환
        return s[length // 2 - 1:length // 2 + 1]