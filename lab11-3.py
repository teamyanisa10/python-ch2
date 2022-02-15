try:
    k = 9//6 # raises divide by zero exception.
    print(k)
    
    
except ZeroDivisionError:   
    print("หารด้วยศูนย์ไม่ได้")
        
finally:
    print('สิ่งนี้ถูกดำเนินการเสมอ')
    
    print("โดย นางสาวญาณิศา เชื้อชัยนาท")