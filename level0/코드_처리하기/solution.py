def solution(code):
   ret = ''    # 결과 문자열
   mode = 0    # 시작 mode는 0
   
   # code의 각 문자와 인덱스를 순회
   for idx, char in enumerate(code):
       if mode == 0:  # mode가 0일 때
           if char != "1":  # 문자가 1이 아니면
               if idx % 2 == 0:  # 짝수 인덱스일 때만
                   ret += char
           else:  # 문자가 1이면
               mode = 1  # mode 변경
       else:  # mode가 1일 때
           if char != "1":  # 문자가 1이 아니면
               if idx % 2 == 1:  # 홀수 인덱스일 때만
                   ret += char
           else:  # 문자가 1이면
               mode = 0  # mode 변경
               
   return ret if ret else "EMPTY"