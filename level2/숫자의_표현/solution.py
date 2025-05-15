def solution(n):
    count = 0
    
    for start in range(1, n + 1):
        sum_val = 0
        
        for num in range(start, n + 1):
            sum_val += num
            
            if sum_val == n:
                count += 1
                break

            if sum_val > n:
                break
                
    return count