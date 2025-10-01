#Viet ham tinh dien tich tam giac
import math
print("=====================")
print("Tinh dien tich tam giac")
print("=====================")

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

def kiemtra(a, b, c):
    if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a:
        return False
    else:
        return True
def dientich(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt( (p * (p - a) * (p - b) * (p - c)))
    return s

if (kiemtra(a, b, c)==True):
    print("Dien tich tam giac la: ", dientich(a, b, c))
else:
    print("Khong phai la tam giac")


