def solution(arr, delete_list):
    result = []

    for x in arr:
        if x not in delete_list:    # delete_list에 없는 원소만
            result.append(x)        # 결과 리스트에 추가
            
    return result