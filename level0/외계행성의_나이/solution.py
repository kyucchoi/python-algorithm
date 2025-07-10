def solution(age):
    answer = ''

    for i in str(age):
        answer += chr(ord(i) + 49)  # 아스키 코드 49는 'a'
        
    return answer