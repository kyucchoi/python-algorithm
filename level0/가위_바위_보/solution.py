def solution(rsp):
    answer = ''
    
    for digit in rsp:
        if digit == '0':
            answer += '5'
        elif digit == '2':
            answer += '0'
        elif digit == '5':
            answer += '2'
            
    return answer