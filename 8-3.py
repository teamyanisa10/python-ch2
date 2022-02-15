def triangle():
    b = int(base.get())
    h = int(high.get())
    area = 1/2*b*h
    messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f" % area)

from tkinter import*
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่่ โดย ญาณิศา เชื้อชัยนาท")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main, text="รับค่าฐาน:", font=("Tahoma",18))
lb1.place(x=10, y=20)
tb1 = Entry(main, textvariable=base)
tb1.place(x=200, y=30, width=300, height=40)

lb2 = Label(main, text="รับค่าสูง:", font=("Tahoma",18))
lb2.place(x=20, y=80)
tb2 = Entry(main, textvariable=high)
tb2.place(x=200, y=80, width=300, height=40)

btu = Button(main, text"คำนวณ", font=("Tahoma",18), command= triangle)
btu.place(x=200, y=100)

lb3 = Label(main, text="คำตอบ:", font=("Tahoma",18))
lb3.place(x=10, y=20)

