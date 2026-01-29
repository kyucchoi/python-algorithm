def solution(n, t, m, p):
    all_digits = ''
    num = 0
    
    while len(all_digits) < t * m:
        all_digits += convert_base(num, n)
        num += 1
    
    answer = ''

    for i in range(t):
        # p번째 사람 차례 = (p - 1) + m * i
        index = (p - 1) + m * i
        answer += all_digits[index]
    
    return answer

def convert_base(num, base):
    if num == 0:
        return '0'
    
    digits = '0123456789ABCDEF'
    result = ''
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result