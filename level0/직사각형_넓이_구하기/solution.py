def solution(dots):
    # x좌표들과 y좌표들을 분리
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    
    # 가로 길이 = x좌표 최댓값 - 최솟값
    width = max(x_coords) - min(x_coords)
    
    # 세로 길이 = y좌표 최댓값 - 최솟값  
    height = max(y_coords) - min(y_coords)
    
    # 넓이 = 가로 × 세로
    return width * height