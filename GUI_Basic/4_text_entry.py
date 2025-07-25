from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0: 0번째 column위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

