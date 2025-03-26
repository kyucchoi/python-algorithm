# 방법 1
import datetime

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    day = datetime.datetime(2016, a, b).weekday()

    return days[day]

# 방법 2
def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일부터 a월 b일까지의 총 일수 계산
    total_days = b - 1  # 1월 1일부터 시작하므로 당일은 제외
    
    # 이전 달까지의 일수 더하기
    for i in range(a - 1):
        total_days += months[i]
    
    # 요일 계산 (1월 1일이 금요일이므로 인덱스 0이 금요일)
    return days[total_days % 7]