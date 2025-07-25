# def std_weight(height, gender):
#     if gender == "남자":
#         weight = height ** 2 * 22 * 0.01**2
#     else:
#         weight = height ** 2 * 21 * 0.01**2

#     print(f"키 {height}cm {gender}의 표준 체중은 {weight:.2f}kg 입니다.") 

# std_weight(175, "여자")

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = "남자"
weight = std_weight(height /100 ,gender)

print(f"키 {height}cm {gender}의 표준 체중은 \
      {weight:.2f}kg입니다.")



