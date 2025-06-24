# 방법 1
def solution(land):
    # land 배열을 직접 수정하여 공간 절약
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
    
    return max(land[-1])

# 방법 2
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[-1])