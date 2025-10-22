str = input()  # 문자열 입력받기
result = ''    # 결과를 저장할 빈 문자열

for char in str:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)