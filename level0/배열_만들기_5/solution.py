def solution(intStrs, k, s, l):
   result = []
   
   for string in intStrs:
       # s부터 s+l까지의 부분 문자열을 잘라내서 정수로 변환
       num = int(string[s:s+l])
       
       # k보다 크면 결과 리스트에 추가
       if num > k:
           result.append(num)
           
   return result