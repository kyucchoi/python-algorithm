def solution(id_pw, db):
    input_id, input_pw = id_pw
    
    # db에서 각 회원정보 확인
    for user_info in db:
        user_id, user_pw = user_info
        
        # 아이디와 패스워드가 모두 일치
        if user_id == input_id and user_pw == input_pw:
            return 'login'
    
    # 아이디만 일치하는 회원이 있는지 확인
    for user_info in db:
        user_id, user_pw = user_info
        
        # 아이디는 일치하지만 패스워드가 다름
        if user_id == input_id:
            return 'wrong pw'
    
    # 아이디가 일치하는 회원이 없음
    return 'fail'