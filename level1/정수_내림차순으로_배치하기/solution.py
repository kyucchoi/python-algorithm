def solution(n):
    # 정수를 문자열로 변환
    str_n = str(n)
    
    # 문자열의 각 문자를 정렬 (내림차순)
    sorted_digits = sorted(str_n, reverse = True)
    
    # 정렬된 문자들을 다시 하나의 문자열로 합침
    sorted_str = ''.join(sorted_digits)
    
    # 문자열을 정수로 변환하여 반환
    return int(sorted_str)