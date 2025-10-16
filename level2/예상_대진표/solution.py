# 방법 1
def solution(n, a, b):
    round_count = 0
    
    while a != b:
        # 다음 라운드 번호로 변경
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_count += 1
    
    return round_count

# 방법 2
def solution(n, a, b):
    round_count = 0
    
    while True:
        round_count += 1
        
        # 다음 라운드 번호 계산
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        # 같은 번호 = 만남
        if a == b:
            return round_count