def solution(my_strings, parts):
   answer = ''
   
   # my_strings와 parts를 동시에 순회
   for string, part in zip(my_strings, parts):
       s, e = part  # 시작과 끝 인덱스
       answer += string[s:e + 1]  # 부분 문자열 추출하여 이어붙이기
       
   return answer