import heapq

def solution(scoville, K):
    # 리스트를 최소 힙으로 변환 (O(n) 시간복잡도)
    heapq.heapify(scoville)
    
    # 음식을 섞은 횟수를 카운트
    mix_count = 0
    
    # 가장 맵지 않은 음식(힙의 루트)이 K 미만인 동안 반복
    while scoville[0] < K:
        # 음식이 1개만 남았는데 K보다 작으면 불가능
        # 더 이상 섞을 수 없으므로 -1 반환
        if len(scoville) == 1:
            return -1
        
        # 가장 맵지 않은 음식 추출 (힙에서 최솟값 제거)
        first = heapq.heappop(scoville)
        
        # 두 번째로 맵지 않은 음식 추출 (남은 힙에서 최솟값 제거)  
        second = heapq.heappop(scoville)
        
        # 새로운 음식의 스코빌 지수 계산
        # 공식: 가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)
        new_scoville = first + (second * 2)
        
        # 새로운 음식을 힙에 추가 (자동으로 힙 구조 유지)
        heapq.heappush(scoville, new_scoville)
        
        # 섞은 횟수 증가
        mix_count += 1
    
    # while문이 끝났다는 것은 scoville[0] >= K 라는 의미
    # 가장 작은 값이 K 이상이면 모든 값이 K 이상이므로 성공
    return mix_count