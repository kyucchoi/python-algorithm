def solution(n, m, section):
    count = 0
    painted = 0

    for s in section:
        if s > painted:
            count += 1
            painted = s + m - 1
    
    return count