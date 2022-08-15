from tkinter import *

root = Tk()
root.title('제목을 여기에 적으면 됩니다. str')
root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

chv1 = IntVar() #chv에 int 형으로 값을 저장한다.
chb1 = Checkbutton(root, text = "오늘 하루 즐겁게 놀기" , variable = chv1) # variable 은 체크가 됐을때 해제됐을때 값을 변수에 저장해주는 명령임
chb1.pack()

chv2 = IntVar() #chv에 int 형으로 값을 저장한다.
chb2 = Checkbutton(root, text = "내일 하루 즐겁게 놀기" , variable = chv2) # variable 은 체크가 됐을때 해제됐을때 값을 변수에 저장해주는 명령임
chb2.pack()
'''
chb.select() # 자동 선택 처리, 기본으로 선택이 되어있음
chb.deselect() # 자동 비선택 처리, 기본으로 선택이 되어있지 않음
'''



def btncmd():
    print("chv1 Value : ", chv1.get())  # .get 이걸 써야 입력값이든 이벤트 값을 가져올 수 있음
    print("chv2 Value : ", chv2.get())
btn = Button(root, text = "click", command = btncmd)
btn.pack()

#print("chv Value : ", chv)

root.mainloop()