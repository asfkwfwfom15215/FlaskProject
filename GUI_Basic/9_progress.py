import time
import tkinter.ttk as ttk
from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms마다 움직임 
# progressbar.pack()

# def btncmd():
#     progressbar.stop() #작동 중지


# btn = Button(root, text = "중지", command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length =150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())



btn = Button(root, text = "시작", command = btncmd2)
btn.pack()



root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

