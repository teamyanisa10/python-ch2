def cal():
    r = int(tb1.get())
    circle = (22/7)*r*r
    mesagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f"+str(circle))
    result.set(circle)
    
from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย ญาณิศา เชื้อชัยนาท")

result = StringVar()

lb = Label(window , text="ยินดีต้อนรับเข้าสู่ python",font=("FreesiaUPC",24))
lb.place(x=50,y=100)

lb2 = Label(window , text="รับค่ารัศมี", font=("FreesiaUPC",24))
lb2.place(x=50,y=100)

tb1 = Entry(window)
tb1.place(x=180,y=110,width=200,height=30)

lb3 = Label(window , text="ผลลัพธ์", font=("FreesiaUPC",24))
lb3.place(x=50,y=150)

tb2 = Entry(window,textvarable=result)
tb2.place(x=180,y=170,width=200,height=30)

btu = Button(window,text="คำนวณ", font=("FreesiaUPC",18),command=cal)
btu.place(x=370,y=100)

window.mainloop()


