from distutils import ccompiler
from msilib.schema import ComboBox
import tkinter.ttk as ttk
from tkinter import *
import pandas as pd

root = Tk()
root.title('NDBC buoyant data')
root.geometry("640x340+300+300") # 창의 가로* 세로 + x좌표 + y좌표 (이걸 다 붙여서 써야함. 뛰어쓰기를 하면 오류뜸)

date = [str(i) for i in range(1,32)] # 1부터 31까지 숫자 생성
month = [str(ii) for ii in range(1,13)]
year = [str(iii) for iii in range(2022,2024)]
hour = [str(iiii) for iiii in range(0,24)]
minute = [str(v) for v in range(0,70,10)]

# 년 콤보박스
yearL = ttk.Combobox(root, height = 10, values = year)
yearL.pack()
yearL.set("년 선택") # 목록 누르기 전에 나오는 것

# 월 콤보박스
monthL = ttk.Combobox(root, height = 10, values = month)
monthL.pack()
monthL.set("월 선택") # 목록 누르기 전에 나오는 것

# 날짜 콤보박스
dateL = ttk.Combobox(root, height = 10, values = date)
dateL.pack()
dateL.set("일 선택") # 목록 누르기 전에 나오는 것

# 시간 콤보박스
hourL = ttk.Combobox(root, height = 10, values = hour)
hourL.pack()
hourL.set("시간 선택") # 목록 누르기 전에 나오는 것

# 분 콤보박스
minuteL = ttk.Combobox(root, height = 10, values = minute)
minuteL.pack()
minuteL.set("분 선택") # 목록 누르기 전에 나오는 것

def btncmd():
    global findex
# 날짜
    a = dateL.get()
    aa = a.zfill(2) # 날짜앞에 0을 붙이고 문자열로 받음
    b = monthL.get()
    bb = b.zfill(2)
    cc = yearL.get()
    dd = cc + bb + aa
# 시간
    h = hourL.get()
    hh = h.zfill(2)
    m = minuteL.get()
    mm = m.zfill(2)
    zz = "00"
    ee = hh + mm + zz
# 기호
    sp = ' '
    hp = '-'
    sc = ':'
    sdate = str(dd)
    stime = str(ee)
    findex = sdate[0:4] + hp + sdate[4:6] + hp + sdate[6:] + sp + stime[0:2] + sc + stime[2:4] + sc + stime[4:]
    print(findex)



btn1 = Button(root, text = "click", command = btncmd)
btn1.pack()

root.mainloop()