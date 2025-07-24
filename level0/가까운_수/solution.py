def solution(array, n):
    closest = array[0]
    min_diff = abs(array[0] - n)
    
    for num in array:
        diff = abs(num - n)
        
        # 더 가까운 수를 찾았거나, 같은 거리인데 더 작은 수인 경우
        if diff < min_diff or (diff == min_diff and num < closest):
            closest = num
            min_diff = diff
    
    return closest