# 방법 1
def solution(M, N):
    max_len = max(M, N)
    min_len = min(M, N)
    
    if max_len == 1:
        return 0
    else:
        return max_len * min_len - 1
    
# 방법 2
def solution(M, N):
    return M * N - 1