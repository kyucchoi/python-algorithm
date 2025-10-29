# 방법 1
def solution(number, limit, power):
    def count_divisors(n):
        count = 0

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1

                if i != n // i:
                    count += 1

        return count
    
    total = 0

    for knight in range(1, number + 1):
        divisors = count_divisors(knight)
        
        if divisors > limit:
            total += power
        else:
            total += divisors
    
    return total

# 방법 2
def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        count = 0
        
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i * i == num:
                    count += 1
                else:
                    count += 2
                    
        if count > limit:
            answer += power
        else:
            answer += count
            
    return answer