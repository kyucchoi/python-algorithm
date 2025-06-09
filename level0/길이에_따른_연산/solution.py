def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        result = 1 # 곱셈의 시작값을 1로 설정 (0으로 하면 모든 결과가 0이 됨)

        for num in num_list:
            result *= num
            
        return result