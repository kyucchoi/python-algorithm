# 방법 1
def solution(participant, completion):
    hash_dict = {}
    
    for person in participant:
        hash_dict[person] = hash_dict.get(person, 0) + 1
    
    for person in completion:
        hash_dict[person] -= 1
    
    for person, count in hash_dict.items():
        if count > 0:
            return person

# 방법 2
def solution(participant, completion):
    participants = {}
    
    # 참가자 이름을 딕셔너리에 추가하고 등장 횟수를 카운트
    for name in participant:
        if name in participants:
            participants[name] += 1
        else:
            participants[name] = 1
    
    # 완주자 이름을 딕셔너리에서 찾아 카운트 감소
    for name in completion:
        participants[name] -= 1
    
    # 딕셔너리에서 값이 0이 아닌(완주하지 못한) 선수 찾기
    for name, count in participants.items():
        if count > 0:
            return name
        
# 방법 3
from collections import Counter

def solution(participant, completion):
    # Counter 객체는 요소의 등장 횟수를 세는 딕셔너리처럼 동작
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    # 두 Counter의 차이는 완주하지 못한 선수를 나타냄
    result = participant_counter - completion_counter
    
    # Counter에서 남은 단 하나의 키(완주하지 못한 선수 이름)를 반환
    return list(result.keys())[0]

# 방법 4
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            
    return participant[-1]