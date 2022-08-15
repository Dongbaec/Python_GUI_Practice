from tkinter import *

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')


btn1 = Button(root, text = "버튼 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text = "버튼2") #pad x 가로 여백 pad y 세로 여백 글자가 많아지면 길이가 변함
btn2.pack()

btn3 = Button(root, width = 5, height = 10, text = "버튼4") # width, height 는 고정된 가로 세로 길이다. 글자가 많아져도 변하지 않는다ㅣ
btn3.pack()

btn4 = Button(root, fg = "red", bg = "yellow", text = "비상탈출") # fg: 글자 색깔 bg: 배경 색깔
btn4.pack()

poto = PhotoImage(file = "gui_pra/go.png")
btn5 = Button(root, image= poto)
btn5.pack()

def btnclick():
    print("버튼이 클릭되었어요")


btn6 = Button(root, text = "동작하는 버튼", command = btnclick)
btn6.pack()


root.mainloop()