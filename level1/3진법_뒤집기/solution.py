# 방법 1
def solution(n):
    # 10진법 -> 3진법으로 변환
    ternary = ""

    while n > 0:
        ternary += str(n % 3)
        n //= 3
    
    # 이미 3진법 숫자를 뒤집은 상태로 만들었으므로 다시 뒤집을 필요 없음
    
    # 3진법 -> 10진법으로 변환
    result = 0

    for i in range(len(ternary)):
        result += int(ternary[i]) * (3 ** (len(ternary) - i - 1))
    
    return result

# 방법 2
def solution(n):
    # 10진법 -> 3진법 (뒤집힌 상태)
    ternary = ""
    
    while n > 0:
        ternary += str(n % 3)
        n //= 3
    
    # 3진법 -> 10진법
    return int(ternary, 3)