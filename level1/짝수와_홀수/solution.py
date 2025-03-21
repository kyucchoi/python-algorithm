def solution(num):
    if num % 2 == 0:    # 2로 나눈 나머지가 0이면 짝수
        return 'Even'
    else:               # 2로 나눈 나머지가 1이면 홀수
        return 'Odd'