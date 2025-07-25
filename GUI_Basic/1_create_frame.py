from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 위치+y좌표 위치

root.resizable(True, True) # x(너비), y(높이) 값 변경 불가, (창 사이즈 크기 변경불가)

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

