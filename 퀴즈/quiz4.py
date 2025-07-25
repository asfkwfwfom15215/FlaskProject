from random import *
#list = [1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
#print(sample(list,2))


# stu_lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(stu_lst)
# chicken_stu = sample(stu_lst,1)[0]
# stu_lst.remove(chicken_stu)
# coffee_stu = sample(stu_lst,3)

users = range(1,21)
#print(type(users))
users = list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4) # 4명중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 -- ")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다 --")


# print("-- 당첨자 발표 -- ")
# print(f"치킨 당첨자 : {chicken_stu}")
# print(f"커피 당첨자 : {coffee_stu}")
# print("-- 축하합니다 --")