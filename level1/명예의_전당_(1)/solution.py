# 방법 1
def solution(k, score):
    hall_of_fame = []
    answer = []
    
    for daily_score in score:
        hall_of_fame.append(daily_score)
        hall_of_fame.sort(reverse=True)
        
        if len(hall_of_fame) > k:
            hall_of_fame.pop()
            
        answer.append(min(hall_of_fame))
        
    return answer

# 방법 2
import heapq

def solution(k, score):
    heap = []
    answer = []
    
    for s in score:
        heapq.heappush(heap, s)
        
        if len(heap) > k:
            heapq.heappop(heap)

        answer.append(heap[0])
    
    return answer