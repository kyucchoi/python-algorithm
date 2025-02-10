def solution(arr):
    # 현재 배열의 길이
    length = len(arr)
    
    # 2의 거듭제곱 중 length보다 크거나 같은 최소값 찾기
    target_length = 1
    
    while target_length < length:
        target_length *= 2
    
    # 필요한 만큼 0 추가
    return arr + [0] * (target_length - length)