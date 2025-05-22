def solution(people, limit):
    people.sort()  # 몸무게 오름차순 정렬
    
    left = 0  # 가장 가벼운 사람의 인덱스
    right = len(people) - 1  # 가장 무거운 사람의 인덱스
    
    boats = 0  # 필요한 구명보트 수
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있는지 확인
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람도 태움
        
        # 무거운 사람은 항상 태움 (혼자서라도)
        right -= 1
        boats += 1
    
    return boats