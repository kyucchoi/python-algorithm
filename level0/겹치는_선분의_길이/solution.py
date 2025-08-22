def solution(lines):
    count = [0] * 201  # -100부터 100까지 (인덱스 0 = -100)
    
    for start, end in lines:
        for i in range(start, end):  # 끝점은 포함하지 않음
            count[i + 100] += 1  # -100을 0으로 맞추기 위해 +100
    
    result = 0
    
    for c in count:
        if c >= 2:
            result += 1
    
    return result