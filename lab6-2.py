f = open("myfile2.txt","w")
txt1="Siam Dhurakit \n"
txt1 += "ญาณิศา เชื้อชัยนาท \n"  
txt1 += "Tel.0929724585"
s = f.write(txt1 )

f.close()

print("เขียนลงไฟล์แล้ว")