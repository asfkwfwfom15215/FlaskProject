# name = "http://google.com"

# index = name.index('.')
# rename = name[7:10]
# total_count = len(name[7:index])
# letter_count = name.count('e')

# print(f"생성된 비밀번호 : {rename}{total_count}{letter_count}!")

#url = "http://naver.com"
#url = "http://daum.com"
url = "http://youtube.com"

my_str = url.replace("http://", "")# 규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print("{0}의 비밀번호는 {1} 입니다.".format(url,password))





