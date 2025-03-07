def solution(absolutes, signs):
    total = 0
    
    for i in range(len(absolutes)):
        # signs[i]가 True이면 양수, False이면 음수
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]
            
    return total