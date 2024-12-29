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