#Viet ham choi game doan so
import random
print("=====================")
print("Game doan so")
print("=====================")
def doanso(x):
    
    while True:
        so = random.randint(1, 100)
        count = 0
        while count <7:
            count += 1
            print("Ket qua doan lan thu: ", count)
            if x < so:
                print("So ban doan nho hon so can doan")
                x = int(input("Moi ban doan lai: "))
                Win = False
            elif x > so:
                print("So ban doan lon hon so can doan")
                x = int(input("Moi ban doan lai: "))
                Win = False
            else:
                print("Chuc mung ban da doan dung")
                Win = True
        if Win == True:
            print("Ban da doan dung sau ", count, " lan doan")
            break
        else:
            print("Ban da het so lan doan. So can doan la: ", so)
            print("Ban muon choi lai khong? (Y/N)")
            tl = input()
            if tl == 'N' or tl == 'n':
                break
x = int(input("Moi ban doan so tu 1 den 100: "))
doanso(x)

