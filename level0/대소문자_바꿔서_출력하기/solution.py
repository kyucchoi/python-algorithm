str = input()  # 문자열 입력받기
result = ''    # 결과를 저장할 빈 문자열

# 각 문자를 순회하면서 대소문자 변환
for char in str:
    if char.isupper():  # 대문자인 경우
        result += char.lower()
    else:               # 소문자인 경우
        result += char.upper()

print(result)