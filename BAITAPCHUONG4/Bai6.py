#Những giá trị nào có thể xuất hiện khi chạy randrange(0, 100)? 
# 4.5 , 34 , -1,  100,  0,  99

import random
print("================================================================")
print("Những giá trị nào có thể xuất hiện trong  randrange(0, 100)")
print("================================================================")

def list():
    values = set()
    while len(values)<100:
        num =  random.randrange(0,100)
        values.add(num)
    return sorted(values)

result = list()
print("Cac gia tri co the xuat hien: ")
for value in result:
    print(value,end="\t")