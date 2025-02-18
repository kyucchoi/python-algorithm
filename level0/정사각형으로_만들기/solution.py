def solution(arr):
    rows = len(arr)        # 행의 수
    cols = len(arr[0])     # 열의 수
    max_len = max(rows, cols)  # 더 큰 쪽의 길이
    
    # 행이 더 많은 경우 (열 추가)
    if rows >= cols:
        return [row + [0] * (max_len - cols) for row in arr]
    
    # 열이 더 많은 경우 (행 추가)
    else:
        result = [row[:] for row in arr]  # 기존 배열 복사
        
        for _ in range(max_len - rows):
            result.append([0] * cols)      # 0으로 채운 행 추가

        return result