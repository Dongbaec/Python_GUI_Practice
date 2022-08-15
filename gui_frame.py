from tkinter import *

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')
root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

root.resizable(False, False) # 가로, 세로 크기 변경 불가
# 위젯을 만들 수만 있으면 자유롭게 할 수 있음

root.mainloop()