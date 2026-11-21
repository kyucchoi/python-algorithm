# 방법 1
def solution(t, p):
    n = len(p)
    target = int(p)
    count = 0

    for i in range(len(t) - n + 1):
        if int(t[i:i + n]) <= target:
            count += 1
            
    return count