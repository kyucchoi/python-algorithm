def solution(x):
    # 각 자릿수의 합 구하기
    # digit_sum = sum(int(digit) for digit in str(x))
    
    str_x = str(x)
    
    digit_sum = 0
    
    for digit in str_x:
        digit_sum += int(digit)

    # 원래 수가 자릿수 합으로 나누어 떨어지는지 확인
    return x % digit_sum == 0