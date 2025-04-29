def solution(today, terms, privacies):
    # 날짜를 일수로 변환하는 함수
    def to_days(date_str):
        year, month, day = map(int, date_str.split('.'))
        return year * 12 * 28 + month * 28 + day
    
    # 오늘 날짜를 일수로 변환
    today_days = to_days(today)
    
    # 약관별 유효기간을 딕셔너리로 정리
    terms_dict = {}
    
    for term in terms:
        type_code, valid_month = term.split()
        terms_dict[type_code] = int(valid_month) * 28  # 유효기간을 일수로 변환
    
    # 파기해야 할 개인정보 번호 목록
    expired_info = []
    
    # 각 개인정보 확인
    for i, privacy in enumerate(privacies, 1):  # 번호는 1부터 시작
        # 수집일자와 약관 종류 분리
        collect_date, term_type = privacy.split()
        # 수집일자를 일수로 변환
        collect_days = to_days(collect_date)
        # 유효기간 만료일 계산
        expiry_days = collect_days + terms_dict[term_type] - 1  # 당일까지 유효하므로 -1
        
        # 만료일이 오늘보다 이전이면 파기 대상
        if expiry_days < today_days:
            expired_info.append(i)
            
    return expired_info