from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정

btn1 = Button(root, text = "버튼1") #Button이라는 위젯을 넣어준다. root에다 text속성을 넣어준다
btn1.pack() #이걸 써줘야만 윈도우에 포함이된다.

btn2 = Button(root, padx=5, pady=10, text = "버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text = "버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", text = "버튼5")
btn5.pack()

photo = PhotoImage(file = "GUI_Basic/image.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

