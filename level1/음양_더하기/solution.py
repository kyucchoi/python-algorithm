# 방법 1
def solution(absolutes, signs):
    total = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]
            
    return total

# zip 함수 사용
def solution(absolutes, signs):
    answer = 0

    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
            
    return answer