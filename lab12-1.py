def Login():
    username = str(tb1.get())
    password = str(tb2.get())
    if username == "admin" and password == "1234" :
       messagebox.showinfo(title = "ผลลัพธ์", message = "ถูกต้อง")
    else :
       messagebox.showinfo(title = "ผลลัพธ์", message = "ไม่ถูกต้อง")
       
from tkinter import *
main = Tk()
main.geometry("800x500")
main.title("โปรแกรมรับค่า Username และ Password")
username=StringVar()
Password=StringVar()
answer=StringVar()

lb1 = Label(main, text="username", font=("FreesiaUPC",20))
lb1.place(x=70, y=40)
lb1 = Label(main, text="password", font=("FreesiaUPC",20))
lb1.place(x=70, y=100)

tb1=Entry(main)
tb1.place(x=200, y=45, width=200, height=25)
tb2=Entry(main)
tb2.place(x=200, y=105, width=200, height=25)


btn=Button(main, text="คำนวณ", font=("FreesiaUPC",20), command=Login)
btn.place(x=450, y=40)

main.mainloop()
