def solution(babbling):
   # 발음 가능한 기본 단어들
   possible = ['aya', 'ye', 'woo', 'ma']
   count = 0
   
   for word in babbling:
       # 각 단어가 발음 가능한지 확인
       temp = word
       
       # 가능한 발음들을 하나씩 제거해보기
       for sound in possible:
           temp = temp.replace(sound, ' ', 1)  # 최대 1번만 치환
       
       # 모든 문자가 제거되었는지 확인 (공백만 남아있어야 함)
       if temp.strip() == '':
           count += 1
   
   return count