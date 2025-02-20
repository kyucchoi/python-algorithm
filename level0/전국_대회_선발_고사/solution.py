def solution(rank, attendance):
    # 참석 가능한 학생만 필터링하고 등수 기준으로 정렬
    available_students = []
    
    for i in range(len(rank)):
        if attendance[i]:
            available_students.append((rank[i], i))  # (등수, 학생 번호) 저장
    
    # 등수 기준 오름차순 정렬
    available_students.sort()
    
    # 상위 3명 선발
    a = available_students[0][1]  # 1등 학생 번호
    b = available_students[1][1]  # 2등 학생 번호
    c = available_students[2][1]  # 3등 학생 번호
    
    # 결과 계산: 10000 × a + 100 × b + c
    return 10000 * a + 100 * b + c