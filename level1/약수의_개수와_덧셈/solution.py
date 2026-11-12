# 방법 1
def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer

# 제곱수의 성질 활용 방법
# 예시 표를 다시 보면, 약수 개수가 홀수인 수는 16과 25뿐
import math

def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if math.isqrt(num) ** 2 == num:
            answer -= num
        else:
            answer += num

    return answer