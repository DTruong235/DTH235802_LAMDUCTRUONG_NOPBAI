#Tính và xuất độ dài đoạn AB 
import math
print("===========================================")
print("Tính và xuất độ dài đoạn AB ")
print("===========================================")

def dodai(xA,yA,xB,yB):
    return math.sqrt(math.pow((xB-xA),2)+math.pow((yB-yA),2))

xA=float(input("Nhap xA: "))
yA=float(input("Nhap yA: "))
xB=float(input("Nhap xB: "))
yB=float(input("Nhap yB: "))

print("Do dai 2 diem la: ",dodai(xA,yA,xB,yB))
    