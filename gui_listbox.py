# 리스트 박스를 활용하면 날짜 입력을 키보드로 입력하는 것이 아니라 마우스로 선택 할 수도 있겠다.
from tkinter import *

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')
root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

lb = Listbox(root, selectmode = "extended", height = 0) # selectmode extended = 여러개 선택 single = 한개 선택 , height = 0 이면 모든 리스트 목록 공개 n 이면 n 개만 공개
lb.insert(0,"apple")
lb.insert(1,"strawberry")
lb.insert(2, "banana")
lb.insert(END, "watermelon")
lb.insert(END, "grape")
lb.pack()

lbsize = lb.size()
def btncmd():
    global i
    i = 0
    #print("선택된 항목:", lb.get(END)) # (,) 시작 인덱스, 끝 인덱스
    a = list(lb.curselection())
    ac = len(a) #리스트의 요소 개수는 len() 함수를 사용한다.

    if ac == 1:
        b = str(a[0]) # 이거 여러개 선택하면 리스트로 반환이 되서 안됨! 암튼 그냥 selectmode를 single로 하면 해결됨 # 이거 반복문 돌리면 해결 ㄱ될 것 가음
        print("선택된 항목 :", lb.get(b))
    else:
        while i < ac :
            b = str(a[i]) # 이거 여러개 선택하면 리스트로 반환이 되서 안됨! 암튼 그냥 selectmode를 single로 하면 해결됨 # 이거 반복문 돌리면 해결 ㄱ될 것 가음
            i = i + 1
            print("선택된 항목 :", lb.get(b))

btn1 = Button(root, text = "click", command = btncmd)
btn1.pack()

root.mainloop()