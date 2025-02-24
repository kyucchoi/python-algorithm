def solution(n):
    # 숫자를 문자열로 변환
    str_n = str(n)
    
    # 각 자릿수를 더할 리스트 생성
    digits = []
    
    # 각 문자를 숫자로 변환하여 리스트에 추가
    for digit in str_n:
        digits.append(int(digit))
    
    # 모든 숫자 더하기
    return sum(digits)