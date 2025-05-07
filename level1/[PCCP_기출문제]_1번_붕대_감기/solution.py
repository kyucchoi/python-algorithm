def solution(bandage, health, attacks):
    # 데이터 추출
    casting_time, heal_per_sec, bonus_heal = bandage
    max_health = health  # 최대 체력 저장
    current_health = health  # 현재 체력 초기화
    
    # 공격 시간을 키로, 데미지를 값으로 하는 딕셔너리 생성
    attack_dict = {time: damage for time, damage in attacks}
    
    # 마지막 공격 시간 구하기
    last_attack_time = attacks[-1][0]
    
    # 연속 성공 시간 초기화
    consecutive_success = 0
    
    # 시간 경과에 따른 시뮬레이션
    for current_time in range(1, last_attack_time + 1):
        # 공격 받는 시간인 경우
        if current_time in attack_dict:
            current_health -= attack_dict[current_time]  # 체력 감소
            consecutive_success = 0  # 연속 성공 초기화
            
            # 체력이 0 이하면 사망
            if current_health <= 0:
                return -1
        
        # 공격 받지 않는 시간인 경우
        else:
            # 체력 회복 (초당 회복량)
            current_health += heal_per_sec
            consecutive_success += 1  # 연속 성공 시간 증가
            
            # 연속 성공 보너스 체크
            if consecutive_success == casting_time:
                current_health += bonus_heal  # 추가 회복
                consecutive_success = 0  # 연속 성공 초기화
            
            # 최대 체력을 초과하지 않도록 제한
            current_health = min(current_health, max_health)
    
    # 모든 공격을 견딘 후 남은 체력 반환
    return current_health