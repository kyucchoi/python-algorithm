def solution(a, b):
    # 두 수를 이어붙인 결과 만들기
    num1 = int(str(a) + str(b))  # a ⊕ b
    num2 = int(str(b) + str(a))  # b ⊕ a
    
    return max(num1, num2)