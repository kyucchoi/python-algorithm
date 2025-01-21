def solution(num_list):
    # 리스트 정렬
    sorted_list = sorted(num_list)
    
    # 앞에서 5개를 제외한 나머지 반환
    return sorted_list[5:]