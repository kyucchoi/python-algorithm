def solution(nums):
    # 선택할 수 있는 폰켓몬의 수
    pick = len(nums) // 2
    
    # 폰켓몬 종류의 수
    pokemon_types = len(set(nums))
    
    # 둘 중 더 작은 값을 반환
    return min(pick, pokemon_types)