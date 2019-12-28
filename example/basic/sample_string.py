# 대/소문자 변환, 원본은 값이 변경 안됨.
a = "Hello Python Programming..."

print("Original : " + a)
print("upper()  : " + a.upper())
print("lower()  : " + a.lower())
print("\n")

# 앞/뒤 문자열 공백 제거
b = "   안녕하세요?   "

print("Original : " + b)
print("strip()  : " + b.strip())
print("\n")

# 문자열 찾기
c = "안녕 안녕 하세요"

out_a = c.find("안녕")
out_b = c.rfind("안녕")
print("Original : " + c)
print("fine()   : {}".format(out_a))
print("rfine()  : " + str(out_b))
print("\n")

# 포함 여부 확인
d = "안녕하세요? 좋은 아침입니다."

print("Original : " + d)
print("좋은 in  : {}".format("좋은" in d))
print("저녁 in  : " + str("저녁" in d))

# 자르기
e = "10 20 30 40 50"

out_e = e.split(" ")
print("Original : " + e)
print("split()  : " + str(out_e))
