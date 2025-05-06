def solution(data, ext, val_ext, sort_by):
    # 각 정보의 인덱스 매핑
    info_index = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    # 필터링: ext 값이 val_ext보다 작은 데이터만 선택
    filtered_data = [item for item in data if item[info_index[ext]] < val_ext]
    
    # 정렬: sort_by에 해당하는 값을 기준으로 오름차순 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[info_index[sort_by]])
    
    return sorted_data