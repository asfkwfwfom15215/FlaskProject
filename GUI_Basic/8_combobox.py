import tkinter.ttk as ttk
from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

values = [str(i) + "일" for i in range(1,32)] # 1~ 31 까지의 숫자 반환
combobox = ttk.Combobox(root, height = 5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 10, values=values, state = "readonly")
readonly_combobox.current(0) #0 번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) #선택된 값 표시 
    print(readonly_combobox.get())


btn = Button(root, text = "선택", command = btncmd)
btn.pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

