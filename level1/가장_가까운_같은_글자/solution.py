def solution(s):
    answer = []
    char_positions = {}
    
    for i, char in enumerate(s):
        if char in char_positions:
            answer.append(i - char_positions[char])
        else:
            answer.append(-1)
        
        char_positions[char] = i
    
    return answer