# 방법 1
def solution(brown, yellow):
    total = brown + yellow
    
    # 세로 길이 h는 3부터 시작 (테두리 1줄 + 노란색 최소 1줄 + 테두리 1줄)
    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:  # h가 total의 약수인지 확인
            w = total // h
            
            # 조건 확인: 노란색이 (w - 2) * (h - 2)개인지
            if (w - 2) * (h - 2) == yellow:
                return [w, h]

# 방법 2
def solution(brown, yellow):
    half_peri = (brown + 4) // 2

    for heigth in range(3, half_peri):
        width = half_peri - heigth

        if heigth * width == yellow + brown:
            return [width, heigth]