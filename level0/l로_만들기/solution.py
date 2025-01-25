def solution(myString):
   result = ''
   
   for char in myString:
       # 문자가 'l'보다 앞서면 'l'로 변경
       if char < 'l':
           result += 'l'
       else:
           result += char
           
   return result