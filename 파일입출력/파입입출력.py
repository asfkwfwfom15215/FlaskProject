# score_file = open("score.txt", 'w', encoding = "utf8")
# print("수학점수 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()


#이미 내용이 존재하는 파일에다 뒤에 이어서 쓰는 방식 (append)
# score_file = open("score.txt", 'a', encoding = "utf8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()


#읽기
# score_file = open("score.txt", 'r', encoding = "utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", 'r', encoding = "utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#몇줄인지 모를때 처리방법

# score_file = open("score.txt", 'r', encoding = "utf8")

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()


#리스트 방법

score_file = open("score.txt", 'r', encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end = "")

score_file.close()


