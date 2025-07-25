# print("Python", "Java")
# print("Python", "Java", sep = ",")
# print("Python", "Java", sep = " vs ")
# print("Python", "Java", "JavaScript", sep = " vs ")


# print("Python", "Java", sep = ",", end = "? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file =sys.stdout)
# print("Python", "Java", file =sys.stderr)



#시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}

for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #8개의 공간을 만들고나서 왼쪽정렬
    #score는 4칸 공간 확보하고나서 오른쪽정렬
    


#은행 대기 순번표 
#001, 002, 003, ...

for num in range(1,23):
    print("대기번호 " + str(num).zfill(3))
    # 3 크기만큼의 공간확보하고 비어있는공간에 0을 채워라

answer = input("아무값이나 입력하세요 : ")
print(type(answer))
print("입력한 값은 " + answer + "입니다.")



 



