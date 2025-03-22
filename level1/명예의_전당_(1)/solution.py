# 방법 1
def solution(k, score):
    # 명예의 전당 목록
    hall_of_fame = []
    # 매일 발표되는 최하위 점수
    answer = []
    
    for s in score:
        # 새 점수를 명예의 전당에 추가
        hall_of_fame.append(s)
        # 높은 점수 순으로 정렬
        hall_of_fame.sort(reverse = True)
        # 명예의 전당 크기를 k로 제한
        if len(hall_of_fame) > k:
            hall_of_fame = hall_of_fame[:k]
        # 최하위 점수 추가
        answer.append(hall_of_fame[-1])
    
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