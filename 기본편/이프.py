# weather = input("오늘 날씨는 어때요? : ")
# if weather == '비' or weather == '눈': 
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요없어요")

temp = int(input("기온은 어때요? "))
if temp >= 30:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp < 30:
    print("괜찮은 날씨예요")
elif 0 < temp <= 10:
    print("외투를 챙기세요")
else:
    print("추워요")


