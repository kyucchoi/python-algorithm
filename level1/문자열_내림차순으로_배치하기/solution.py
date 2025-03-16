def solution(s):
    # 문자열을 리스트로 변환
    chars = list(s)
    
    # 내림차순으로 정렬 (reverse = True)
    chars.sort(reverse = True)
    
    # 리스트를 다시 문자열로 변환
    return ''.join(chars)

# 내 방법
def solution(s):
    answer = sorted(s, reverse = True)
    
    return ''.join(answer)