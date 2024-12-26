def solution(todo_list, finished):
    result = []
    
    for i in range(len(todo_list)):
        if not finished[i]:    # finished[i]가 False인 경우
            result.append(todo_list[i])
            
    return result