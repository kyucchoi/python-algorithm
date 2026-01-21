def solution(n, k):
    converted = convert_base(n, k)
    
    numbers = converted.split('0')
    
    count = 0
    
    for num_str in numbers:
        if num_str and is_prime(int(num_str)):
            count += 1
    
    return count

def convert_base(n, k):
    if n == 0:
        return '0'
    
    result = ''

    while n > 0:
        result = str(n % k) + result
        n //= k
    
    return result

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True