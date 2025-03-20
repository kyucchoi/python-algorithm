def solution(d, budget):
    d.sort()  # 신청 금액을 오름차순으로 정렬
    count = 0  # 지원 가능한 부서 수
    
    for amount in d:
        if budget >= amount:  # 예산이 충분하면
            budget -= amount  # 예산에서 신청 금액 차감
            count += 1  # 지원 부서 수 증가
        else:
            break  # 예산 부족 시 반복 종료
    
    return count