# 방법 1
def solution(s):
    chars = list(s)
    
    chars.sort(reverse=True)
    
    return ''.join(chars)

# 방법 2
def solution(s):
    return ''.join(sorted(s, reverse=True))