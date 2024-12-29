def solution(num_list):
   # num_list의 마지막 원소와 그 전 원소 비교
   if num_list[-1] > num_list[-2]:
       # 마지막 원소가 더 크면 차이를 추가
       num_list.append(num_list[-1] - num_list[-2])
   else:
       # 마지막 원소가 더 크지 않으면 두 배 값을 추가
       num_list.append(num_list[-1] * 2)
   
   return num_list