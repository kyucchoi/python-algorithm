def solution(X, Y):
    # 각 숫자의 등장 횟수를 세기 위한 딕셔너리 생성
    x_count = {}
    y_count = {}
    
    # X의 각 숫자 등장 횟수 세기
    for digit in X:
        x_count[digit] = x_count.get(digit, 0) + 1
        
    # Y의 각 숫자 등장 횟수 세기
    for digit in Y:
        y_count[digit] = y_count.get(digit, 0) + 1
    
    # 공통 숫자 찾기
    common_digits = []
    
    for digit in '9876543210':  # 큰 수부터 확인
        if digit in x_count and digit in y_count:
            # 두 문자열에서 공통으로 등장하는 최소 횟수만큼 추가
            count = min(x_count[digit], y_count[digit])
            common_digits.extend([digit] * count)
    
    # 공통 숫자가 없는 경우
    if not common_digits:
        return '-1'
    
    # 결과 문자열 생성
    result = ''.join(common_digits)
    
    # 결과가 0으로만 이루어진 경우
    if result.startswith('0') and result.endswith('0'):
        return '0'
    
    return result