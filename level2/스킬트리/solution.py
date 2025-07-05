def solution(skill, skill_trees):
    count = 0
    
    for skill_tree in skill_trees:
        # 스킬트리에서 선행 스킬에 해당하는 것만 추출
        filtered_skills = ''
        
        for char in skill_tree:
            if char in skill:
                filtered_skills += char
        
        # 추출한 스킬들이 선행 스킬 순서의 앞부분과 일치하는지 확인
        if skill.startswith(filtered_skills):
            count += 1
    
    return count