from tkinter import *

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')
root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

txt = Text(root, width = 30, height = 5) # Text 는 여러줄을 작성해야할 때 쓴다.
txt.pack()
txt.insert(END, "글자를 입력하세요 ") # 이 칸을 누르면 글자가 삭제되겐 못하나?

e = Entry(root, width=30) # Entry는 한줄 만 작성해야할 때 쓴다. 예르들어 아이디나 비밀번호 적는 칸 같은것임
e.pack()

def btncmd():
    # 출력
    print(txt.get("1.0",END)) # 1: 은 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())
    # 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn1 = Button(root, text = "click", command = btncmd)
btn1.pack()

root.mainloop()