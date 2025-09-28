# 방법 1
def solution(k, score):
    hall_of_fame = []
    answer = []
    
    for daily_score in score:
        hall_of_fame.append(daily_score)
        hall_of_fame.sort(reverse = True)
        
        if len(hall_of_fame) > k:
            hall_of_fame.pop()
            
        answer.append(min(hall_of_fame))
        
    return answer

# 방법 2
import heapq

def solution(k, score):
    heap = []  # 최소 힙 사용
    answer = []
    
    for s in score:
        # 힙에 새 점수 추가
        heapq.heappush(heap, s)
        # 힙의 크기가 k를 초과하면 가장 작은 값 제거
        if len(heap) > k:
            heapq.heappop(heap)
        # 현재 힙의 최소값(최하위 점수) 기록
        answer.append(heap[0])
    
    return answer