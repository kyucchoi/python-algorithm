def solution(n, k):
    def convert(num, base):
        if num == 0:
            return '0'

        result = ''

        while num > 0:
            result = str(num % base) + result
            num //= base

        return result
    
    def is_prime(num):
        if num < 2:
            return False

        if num == 2:
            return True

        if num % 2 == 0:
            return False

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True
    
    converted = convert(n, k)

    parts = converted.split('0')
    
    count = 0
    
    for part in parts:
        if part and is_prime(int(part)):
            count += 1
    
    return count