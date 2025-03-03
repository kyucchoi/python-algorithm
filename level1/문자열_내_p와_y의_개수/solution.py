def solution(s):
    # 모든 문자를 소문자로 변환
    s = s.lower()
    
    # 'p'와 'y'의 개수를 세기
    p_count = s.count('p')
    y_count = s.count('y')
    
    # 개수 비교
    return p_count == y_count