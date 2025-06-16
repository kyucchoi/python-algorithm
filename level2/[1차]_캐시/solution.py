# 방법 1
def solution(cacheSize, cities):
    # 캐시 크기가 0이면 모든 검색이 miss
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()  # 대소문자 구분 안 함
        
        if city in cache:
            # Cache Hit: 해당 도시를 최신으로 이동
            cache.remove(city)  # 기존 위치에서 제거
            cache.append(city)  # 맨 뒤에 추가 (최신으로 표시)
            time += 1
        else:
            # Cache Miss: 새로운 도시 추가
            if len(cache) >= cacheSize:
                cache.pop(0)  # 가장 오래된 것(맨 앞) 제거
            cache.append(city)  # 새 도시 추가
            time += 5
    
    return time

# 방법 2
from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen = cacheSize)
    time = 0

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5
            
    return time