def solution(n, a, b):
    round_num = 1

    while True:
        if (a - 1) // 2 == (b - 1) // 2:  # 같은 대진인가?
            return round_num
        
        a = (a + 1) // 2  # 다음 라운드 번호
        b = (b + 1) // 2
        round_num += 1