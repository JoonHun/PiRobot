# if 조건문 예제
# if elif else 모두 사용

import datetime

# 현재 시간, 날짜 구하기
now = datetime.datetime.now()

print("현재 날짜는 {}년 {}월 {}일 입니다.".format(now.year, now.month, now.day))

if( now.hour < 12):
    print("현재 시간은 오전 {}시 {}분 입니다.".format(now.hour, now.minute))
else:
    print("현재 시간은 오후 {}시 {}분 입니다.".format(now.hour-12, now.minute))

# elif 사용할 때 조건문 잘 사용해야 함. 한번이라도 비교를 줄이기 위하여...
if( 3 <= now.month <= 5 ):
    print("지금은 봄 입니다.")
#elif( 6 <= now.month <= 8 ):
elif( now.month <= 8 ):
    print("지금은 여름 입니다.")
#elif( 9 <= now.month <= 11 ):
elif( now.month-3 <= 11 ):
    print("지금은 가을 입니다.")
else:
    print("지금은 겨울 입니다.")

number = 0

# 아무것도 안함? 구현 안했음?
if( number > 0 ):
    pass
else:
    raise NotImplementedError
