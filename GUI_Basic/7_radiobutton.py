from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text = "햄버거", value=1, variable = burger_var)

btn_burger2 = Radiobutton(root, text = "치즈버거", value=2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "치킨버거", value=3, variable = burger_var)
btn_burger3.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="메뉴를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value = "콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value = "사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음료 중 선택된 값을 출력

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

