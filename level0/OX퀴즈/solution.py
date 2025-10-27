def solution(quiz):
    result = []

    for equation in quiz:
        # 수식을 공백으로 분리
        parts = equation.split(' ')

        # 각 요소 추출
        X = int(parts[0])        # 첫 번째 숫자
        operator = parts[1]      # 연산자 (+ 또는 -)
        Y = int(parts[2])        # 두 번째 숫자
        Z = int(parts[4])        # 결과값

        if operator == '+':
            calculated = X + Y
        elif operator == '-':
            calculated = X - Y

        if calculated == Z:
            result.append('O')
        else:
            result.append('X')

    return result