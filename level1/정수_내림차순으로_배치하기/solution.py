def solution(n):
    digits = str(n)
    sorted_digits = sorted(digits, reverse=True)
    joined = ''.join(sorted_digits)
    answer = int(joined)
    
    return answer

# 한줄로 풀기
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))