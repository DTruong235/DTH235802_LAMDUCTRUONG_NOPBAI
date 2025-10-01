#Viet ham tinh ROI
print("==================")
print("Viet ham tinh ROI")
print("==================")
def ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi>=0.75:
         return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
dt=int(input("Nhập Doanh Thu:"))
cp=int(input("Nhập chi phí:"))
roi=ROI(dt,cp)
print("Tỉ Lệ ROI=",roi)
print("==>",GoiYDauTu(roi))
