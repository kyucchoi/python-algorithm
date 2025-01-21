def solution(my_string, s, e):
   # 문자열을 리스트로 변환
   string_list = list(my_string)
   
   # s부터 e까지의 부분을 뒤집기
   string_list[s:e + 1] = reversed(string_list[s:e + 1])
   
   # 리스트를 다시 문자열로 변환해서 반환
   return ''.join(string_list)