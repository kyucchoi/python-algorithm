# 방법 1
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    
    # 각 자리에서 한 모음으로 시작하는 단어 개수
    # weights[i] = 5^4 + 5^3 + 5^2 + 5^1 + 5^0 (i번째 이후 자리)
    weights = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        char = word[i]
        
        char_idx = vowels.index(char)
        
        answer += char_idx * weights[i] + 1
    
    return answer

# 방법 2
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    answer = 0
    
    for i, char in enumerate(word):
        answer += vowels.index(char) * weights[i] + 1
    
    return answer