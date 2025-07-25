import pickle
# #피클 == 프로그램상에서의 데이터를 파일로 저장하는것
# profile_file = open("profile.pickle", "wb")
# #pickle을 쓰기위해선wb(binary)로정의해줘야함
# profile = {"이름":"박명수", "나이" : 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에저장
# profile_file.close() 

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에불러오기
print(profile)
profile_file.close()
