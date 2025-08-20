def solution(my_string, queries):
    # 문자열을 리스트로 변환 (문자열은 직접 수정이 불가능하므로)
    string_list = list(my_string)
    
    # 각 쿼리 처리
    for s, e in queries:
        # s부터 e까지의 부분을 뒤집기
        string_list[s:e + 1] = reversed(string_list[s:e + 1])
    
    # 리스트를 다시 문자열로 변환
    return ''.join(string_list)