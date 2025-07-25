from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #선택 해제 처리
chkbox.pack()

listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기",variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0 :체크 해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

