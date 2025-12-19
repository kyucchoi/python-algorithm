def solution(num_list):
    multiply = 1

    for num in num_list:
        multiply *= num
        
    sum_square = sum(num_list)**2
    
    return 1 if multiply < sum_square else 0