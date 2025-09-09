def solution(s, n):
    chars = list(s)
    
    for i in range(len(chars)):
        if chars[i].isupper():
            chars[i] = chr((ord(chars[i]) - ord('A') + n) % 26 + ord('A'))
        elif chars[i].islower():
            chars[i] = chr((ord(chars[i]) - ord('a') + n) % 26 + ord('a'))
            
    return ''.join(chars)