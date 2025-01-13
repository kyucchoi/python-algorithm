def solution(str_list):
   # l과 r의 인덱스 찾기
   for i in range(len(str_list)):
       if str_list[i] == 'l':
           return str_list[:i]  # l 왼쪽 부분 반환
       elif str_list[i] == 'r':
           return str_list[i+1:]  # r 오른쪽 부분 반환
           
   return []  # l이나 r이 없는 경우