#Viet ham tinh dien tich tam giac
print("=====================")
print("Tinh dien tich tam giac")
print("=====================")

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if kiemtra(a, b, c):
    print("Dien tich tam giac la: ", dientich(a, b, c))
else:
    print("Khong phai la tam giac")

def kiemtra(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def dientich(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s