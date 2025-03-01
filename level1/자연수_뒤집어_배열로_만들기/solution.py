def solution(n):
    # 숫자를 문자열로 변환
    str_n = str(n)
    
    # 문자열을 뒤집고 각 문자를 정수로 변환하여 리스트에 저장
    # answer = [int(digit) for digit in reversed(str_n)]

    answer =[]

    for digit in reversed(str_n):
        answer.append(int(digit))
    
    return answer