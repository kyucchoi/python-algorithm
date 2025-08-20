def solution(num_list):
    # 모든 원소의 곱 계산
    multiply = 1
    for num in num_list:
        multiply *= num
        
    # 모든 원소의 합의 제곱 계산
    sum_square = sum(num_list) ** 2
    
    # 곱이 합의 제곱보다 작으면 1, 크면 0
    return 1 if multiply < sum_square else 0