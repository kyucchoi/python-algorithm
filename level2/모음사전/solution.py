# 방법 1
from itertools import product

def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for length in range(1, 6):
        for combo in product(vowels, repeat = length):
            words.append(''.join(combo))
    
    words.sort()
    
    return words.index(word) + 1

# 방법 2
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    answer = 0
    
    for i, char in enumerate(word):
        answer += vowels.index(char) * weights[i] + 1
    
    return answer