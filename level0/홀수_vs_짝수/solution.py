def solution(num_list):
    # 홀수 번째(인덱스 0, 2, 4, ...) 원소들의 합
    odd_sum = sum(num_list[::2])
    
    # 짝수 번째(인덱스 1, 3, 5, ...) 원소들의 합
    even_sum = sum(num_list[1::2])
    
    return max(odd_sum, even_sum)