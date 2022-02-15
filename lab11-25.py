def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b ให้ผลลัพธ์เป็น 0")
    else:
        print (c)
  

AbyB(1.0, 3.0)
AbyB(7.0, 2.0)
print("โดย นางสาวญาณิศา เชท้อชัยนาท")