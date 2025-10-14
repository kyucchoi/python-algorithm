def solution(num_list):
    total_count = 0

    for num in num_list:
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num - 1) // 2
                
            total_count += 1
    
    return total_count