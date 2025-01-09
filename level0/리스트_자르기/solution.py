def solution(n, slicer, num_list):
   a, b, c = slicer  # slicer의 세 값을 a, b, c로 분리
   
   if n == 1:
       return num_list[: b + 1]     # 0부터 b까지
   elif n == 2:
       return num_list[a :]       # a부터 끝까지
   elif n == 3:
       return num_list[a : b + 1]    # a부터 b까지
   else:  # n == 4
       return num_list[a : b + 1 : c]  # a부터 b까지 c 간격으로