
def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열('mm:ss')을 초 단위로 변환하는 함수
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    
    # 초 단위를 시간 문자열('mm:ss')로 변환하는 함수
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f'{minutes:02d}:{seconds:02d}'
    
    # 시간 변환
    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    # 초기 위치가 오프닝 구간이면 오프닝 건너뛰기
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    # 명령어 실행
    for cmd in commands:
        if cmd == 'prev':
            # 10초 전으로 이동
            pos_sec = max(0, pos_sec - 10)
        elif cmd == 'next':
            # 10초 후로 이동
            pos_sec = min(video_len_sec, pos_sec + 10)
        
        # 명령 실행 후 오프닝 구간이면 오프닝 건너뛰기
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    
    # 최종 위치를 시간 형식으로 변환하여 반환
    return seconds_to_time(pos_sec)