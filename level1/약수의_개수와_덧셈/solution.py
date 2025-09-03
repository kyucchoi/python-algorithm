def solution(left, right):
    result = 0
    
    for number in range(left, right + 1):
        divisor_count = 0
        
        for divisor in range(1, int(number**0.5) + 1):
            if divisor * divisor == number:
                divisor_count += 1
            elif number % divisor == 0:
                divisor_count += 2
                
        if divisor_count % 2 == 0:
            result += number
        else:
            result -= number
            
    return result