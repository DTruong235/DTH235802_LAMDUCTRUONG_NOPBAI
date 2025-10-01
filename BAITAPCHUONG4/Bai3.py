#viet ham tinh BMI
print("=====================")
print("Tinh chi so BMI")
print("=====================")
def tinhBMI(cannang, chieucao):
    BMI = cannang / (chieucao ** 2)
    return BMI
def kiemtra(cannang, chieucao):
    if cannang <=0 or chieucao <=0:
        return False
    else:
        return True
def phanloai(BMI):

    if bmi<18.5:
        return "Gầy"
    elif bmi<=24.9:
        return "Bình thường"
    elif bmi<=29.9:
        return "Hơi Béo"
    elif bmi<=34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi<=39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp độ 3"

def nguycobenh(BMI):

    if bmi<18.5:
        return "Thấp"
    elif bmi<=24.9:
        return "Trung bình"
    elif bmi<=29.9:
        return "Cao"
    elif bmi<=34.9:
        return "Cao"
    elif bmi<=39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"
    
cannang = float(input("Nhap can nang (kg): "))
chieucao = float(input("Nhap chieu cao (m): "))
if kiemtra(cannang, chieucao)==False:
    print("Can nang hoac chieu cao khong hop le")
else:
    bmi =  tinhBMI(cannang, chieucao)
    print("Chi so BMI cua ban la: ",bmi)
    print("Phan loai: ",phanloai(bmi))
    print("Nguy co benh: ",nguycobenh(bmi))