# 숫자를 문자열로 변환하기
a = "{}만원".format(500)
b = "파이선 열공하여 연봉 {}만원 만들기".format(9000)
c = "{} {} {}".format(3000, 4000, 5000)
d = "{} {} {}".format(1, "문자열", True)

print("\n숫자를 문자로 변화하기")
print(a)
print(b)
print(c)
print(d)

# 숫자
aa = "{:d}".format(52)

# 특정 자리에 출력
bb = "{:5d}".format(52)
cc = "{:10d}".format(52)

# 0 으로 채우기
dd = "{:05d}".format(52)
ee = "{:05d}".format(-52)

print("\n숫자, 특정 자리, 0 으로 채우기")
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)

# 기호와 함께 출력하기
f = "{:+d}".format(52)
g = "{:+d}".format(-52)
h = "{: d}".format(52)
i = "{: d}".format(-52)

print("\n기호와 함께 출력하기")
print(f)
print(g)
print(h)
print(i)

#기호 위치 변경
j = "{:+7d}".format(345)
k = "{:+7d}".format(-345)
l = "{:=+7d}".format(345)
m = "{:=+7d}".format(-345)
n = "{:=+07d}".format(345)
o = "{:=+07d}".format(-345)

print("\n기호 위치 변경하기")
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)

#소수점 자리수 정하기 10자리 중 3자리는 소수점 아래
p = "{:10.3f}".format(3.14)
q = "{:=+010.3f}".format(-2.2)

print("\n소수점 자리수 정하기")
print(p)
print(q)