import tkinter.messagebox as msgbox
from tkinter import * #tkinter모듈안에있는 모든것들을 쓰겠다.

root = Tk()
root.title("GUI배우기") #창 위에 타이틀 설정
root.geometry("640x480") #창 크기 설정  : 가로 * 세로, x를 써줘야함

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료됐습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진됐습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예/아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    msgbox.askyesnocancel(title = None, message = "예매 내역이 저장되지 않았습니다.\n 저장 후 프로그램을 종료료하시겠습니까?")

Button(root, command = info, text = "알림").pack()
Button(root, command = warn, text = "경고").pack()
Button(root, command = error, text = "에러").pack()
Button(root, command = okcancel, text = "확인 취소").pack()
Button(root, command = retrycancel, text = "확인 취소").pack()
Button(root, command = yesno, text = "예 아니오").pack()
Button(root, command = yesnocancel, text = "예 아니오 취소").pack()

root.mainloop() # loop를 통해서 창이 닫히지않도록 해줍니다

