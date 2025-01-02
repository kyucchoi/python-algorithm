def solution(str_list, ex):
   result = ''
   
   for string in str_list:
       # ex가 string에 포함되어 있지 않으면 result에 추가
       if ex not in string:
           result += string
           
   return result