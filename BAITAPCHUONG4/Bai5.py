#Viet ham de quy fibonaci
print("=============================")
print("Chuong trinh de qui fibonaci")
print("=============================")
def fibonacci(n): 
    if n<=2 : 
        return 1 
    return fibonacci(n-1)+fibonacci(n-2) 
 
def listfibo(n): 
    for i in range(1,n+1): 
        print(fibonacci(i),end='\t')

n=int(input("Nhap n: "))
print("Vi tri: ",fibonacci(n))
print("Danh sach: ")
listfibo(n)