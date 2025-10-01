def sum1(n): 
    s = 0 
    while n > 0: 
        s += 1 
        n -= 1 
    return s 
def sum2(): 
    global val 
    s = 0 
    while val > 0: 
        s += 1 
        val -= 1 
    return s 
def sum3(): 
    s = 0 
    for i in range(val, 0, -1): 
        s += 1 
    return s    
#TH1
'''def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum2()) 
    print(sum3()) 
main()'''
'''Kết quả in re sẽ là:
    5
    5
    0
    Vì val là biến toàn cục nên hàm sum2 và sum3 đều sử dụng được biến này.
    Và hàm sum2 làm thay đổi giá trị của val, val = 0.
    Nêm sum3 không thể đếm được gì nên trả về 0.
'''
#TH2
'''def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum3()) 
    print(sum2()) 
main()'''
'''Kết quả in re sẽ là:
    5
    5
    5
    Vì sum3 được gọi trước, giá trị của val không đổi, val = 5.
    Nên khi sum2 được gọi thì val vẫn là 5.
'''

#TH3
'''def main(): 
    global val 
    val = 5 
    print(sum2()) 
    print(sum1(5)) 
    print(sum3()) 
main()'''
'''Kết quả in re sẽ là:
    5
    5
    0
    Vì sum2 được gọi trước nên giá sum = 5 và val = 0.
    Hàm sum1 được truyền tham số bên ngoài nên giá trị bên trong không đổi.
    Hàm sum3 khi được gọi giá trị val = 0 được truyền vào nên trả về 0.
'''