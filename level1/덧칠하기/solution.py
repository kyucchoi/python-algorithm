def solution(n, m, section):
    count = 0  # 페인트칠 횟수
    painted = 0  # 마지막으로 페인트칠한 위치
    
    for s in section:
        # 현재 구역이 이미 칠해져 있으면 건너뜀
        if s <= painted:
            continue
        
        # 페인트칠 횟수 증가
        count += 1
        
        # 롤러로 칠한 마지막 위치 업데이트 (현재 위치 + 롤러 길이 - 1)
        painted = s + m - 1
    
    return count