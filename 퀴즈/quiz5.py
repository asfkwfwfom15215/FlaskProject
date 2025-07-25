from random import *

count = 0
for i in range(1,51):
    customer = randrange(5,51)
    if 5 <= customer <=15:
        match = 'o'
        count +=1
    else:
        match = ''

    print(f"[{match}] {i} 번째 손님 (소요 시간 : {customer}분)")    

print(f"총 탑승 승객 : {count}")        


