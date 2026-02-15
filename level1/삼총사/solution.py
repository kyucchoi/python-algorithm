# 방법 1
def solution(number):
    count = 0
    n = len(number)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    
    return count

# 방법 2
from itertools import combinations

def solution(number):
    count = 0
    
    for combo in combinations(number, 3):
        if sum(combo) == 0:
            count += 1
    
    return count