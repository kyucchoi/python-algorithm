def solution(myString, pat):
   # A와 B를 서로 바꾸기
   swapped = ''
   for char in myString:
       if char == 'A':
           swapped += 'B'
       else:  # char == 'B'
           swapped += 'A'
   
   # 바꾼 문자열에 pat이 있는지 확인
   return 1 if pat in swapped else 0