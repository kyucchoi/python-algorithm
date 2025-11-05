# 방법 1
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()  # 대소문자 구분 안 함
        
        if city in cache:
            # Cache Hit: 해당 도시를 최신으로 이동
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            # Cache Miss: 새로운 도시 추가
            if len(cache) >= cacheSize:
                cache.pop(0)

            cache.append(city)
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