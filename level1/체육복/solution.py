def solution(n, lost, reserve):
    # 학생들의 체육복 상태를 나타내는 배열 (1은 체육복이 있음, 0은 없음)
    students = [1] * (n + 1)  # 0번 인덱스는 사용하지 않음
    
    # 도난당한 학생은 체육복이 0개가 됨
    for l in lost:
        students[l] -= 1
    
    # 여벌이 있는 학생은 체육복이 1개 추가됨
    for r in reserve:
        students[r] += 1
    
    # 체육복 빌려주기
    for i in range(1, n + 1):
        if students[i] == 0:  # 체육복이 없는 학생
            # 앞번호 학생에게 빌리기
            if i > 1 and students[i - 1] > 1:
                students[i - 1] -= 1
                students[i] += 1
            # 뒷번호 학생에게 빌리기
            elif i < n and students[i + 1] > 1:
                students[i + 1] -= 1
                students[i] += 1
    
    # 체육복이 있는(수업을 들을 수 있는) 학생 수 세기
    return sum(1 for i in range(1, n + 1) if students[i] > 0)