from itertools import count
from tkinter import *

i = 0

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')

root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

label1 = Label(root, text = "라벨 이름은 여기에 넣으면 됩니다..")
label1.pack()

poto = PhotoImage(file = "gui_pra/go.png")
label2 = Label(root, image = poto)
label2.pack()


def change():
    global i  # 전역변수를 쓰려면 global을 변수 앞에 써주고 함수 밖에서 전역변수 선언을 먼저 해줘야한다.
    i = i + 1
    if i == 10:
        label1.config(text = "그만 눌러!!!!")
    elif i < 10:
        label1.config(text = "stop click")
    else:
        label1.config(text = "{}번 눌렀습니다.".format(i))

def clearI():
    global i
    i = 0
    label1.config(text = "라벨 이름은 여기에 넣으면 됩니다..")

btn1 = Button(root, text = "click", command = change)
btn1.pack()

btn2 = Button(root, text = "clear", command = clearI)
btn2.pack()


root.mainloop()