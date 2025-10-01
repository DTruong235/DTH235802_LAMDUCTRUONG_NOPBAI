# Viết chương trình tính loga x
import math
print("===============================")
print(" Viết chương trình tính loga x")
print("===============================")

def loga(x,a):
    if x <= 0:
        return "Lỗi: Giá trị x phải > 0"  
    if a <= 0 or a == 1:
        return "Lỗi: Cơ số phải > 0 và khác 1" 
    
    return math.log(x, a)

a = float(input("Nhap co so a: ")) 
x = float(input("Nhap so x: "))
print("Ket qua cua loga x: ", loga(x,a))

