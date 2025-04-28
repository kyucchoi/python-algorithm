def solution(wallpaper):
    # 파일이 있는 위치의 최소/최대 행과 열 초기화
    min_row = min_col = float('inf')
    max_row = max_col = float('-inf')
    
    # 바탕화면을 순회하며 파일 위치 확인
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                # 파일 위치에 따라 최소/최대 행과 열 업데이트
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i + 1)  # 드래그 끝점은 파일 위치 + 1
                max_col = max(max_col, j + 1)  # 드래그 끝점은 파일 위치 + 1
    
    # 드래그 시작점 (min_row, min_col)과 끝점 (max_row, max_col)
    return [min_row, min_col, max_row, max_col]