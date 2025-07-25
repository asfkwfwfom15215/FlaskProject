
# for i in range(1, 51):
#     profile = open(f"{i}주차.txt", 'w' ,encoding = "utf8")

#     profile.write(f" -{i} 주차 주간보고 - \n")
#     profile.write("부서 : \n")
#     profile.write("이름 : \n")
#     profile.write("업무 요약 : \n")
#     profile.close()

for i in range(1,51):
    with open(str(i) + "주차.txt", 'w', encoding = "utf8") as report_file:
        report_file.write(f"{i} 주차 주간보고 -\n")
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")

