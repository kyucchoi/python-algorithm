def solution(myString, pat):
   # pat의 마지막 인덱스 찾기
   last_index = myString.rindex(pat)
   
   # 처음부터 pat이 끝나는 위치까지 자르기
   return myString[:last_index + len(pat)]