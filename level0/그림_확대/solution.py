def solution(picture, k):
    result = []
    
    # 각 행을 k배 확대
    for row in picture:
        # 각 픽셀을 가로로 k번 반복
        scaled_row = ''.join(pixel * k for pixel in row)
        
        # 확대된 행을 세로로 k번 반복해서 결과에 추가
        for _ in range(k):
            result.append(scaled_row)
    
    return result