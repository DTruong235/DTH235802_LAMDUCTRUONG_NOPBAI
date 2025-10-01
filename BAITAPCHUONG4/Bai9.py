import math
print("=========================================")
print("Chương Trình Tính Căn Lồng Nhau")
n = int(input("Nhập n: "))
s = 0
for i in range(n):
    s = math.sqrt(2 + s)
print("S(n) =", s)