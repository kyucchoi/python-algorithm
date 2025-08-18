def solution(common):
   # 1. 등차수열인지 확인
   diff1 = common[1] - common[0]
   diff2 = common[2] - common[1]
   
   # 2. 등차수열인 경우
   if diff1 == diff2:
       return common[-1] + diff1
   # 3. 등비수열인 경우
   else:
       ratio = common[1] // common[0]
       
       return common[-1] * ratio