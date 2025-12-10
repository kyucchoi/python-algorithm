import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    # 최대 힙
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    # n시간 작업
    for _ in range(n):
        max_work = heapq.heappop(heap)
        heapq.heappush(heap, max_work + 1)
    
    # 피로도
    return sum(w**2 for w in heap)