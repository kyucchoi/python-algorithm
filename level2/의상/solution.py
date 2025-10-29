def solution(clothes):
    clothes_dict = {}

    for name, category in clothes:
        clothes_dict[category] = clothes_dict.get(category, 0) + 1
    
    answer = 1
    
    for count in clothes_dict.values():
        answer *= (count + 1)
    
    return answer - 1