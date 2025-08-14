def solution(numlist, n):
    # 정렬 기준: (거리, -숫자값)
    # 거리가 가까운 순으로, 같은 거리면 큰 수부터
    numlist.sort(key=lambda x: (abs(x - n), -x))
    
    return numlist