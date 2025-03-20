# 방법 1
def solution(sizes):
   max_w, max_h = 0, 0
   
   for w, h in sizes:
       # 각 명함을 가로가 더 길도록 회전
       if w < h:
           w, h = h, w
       
       # 최대 가로, 세로 길이 갱신    
       max_w = max(max_w, w)
       max_h = max(max_h, h)
   
   return max_w * max_h

# 방법 2
def solution(sizes):
    max_width = 0
    max_height = 0
    
    for card in sizes:
        # 각 명함을 가로가 더 길게 정렬 (회전 가능)
        width, height = max(card), min(card)
        
        # 현재까지의 최대 가로/세로 길이 업데이트
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    
    # 최종 지갑 크기 = 최대 가로 × 최대 세로
    return max_width * max_height

# 방법 3
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)