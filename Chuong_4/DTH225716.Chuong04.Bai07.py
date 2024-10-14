'''
Tính và xuất độ dài đoạn AB
Yêu cầu:
Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. 
|AB|= Dab = can((xB-xa)^2+(yB-yA)^2)
'''
import math

def tinh_do_dai_AB(xA, yA, xB, yB):
    # Tính độ dài đoạn AB
    do_dai = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
    return do_dai

# Nhập tọa độ điểm A
xA = float(input("Nhập tọa độ x của điểm A: "))
yA = float(input("Nhập tọa độ y của điểm A: "))

# Nhập tọa độ điểm B
xB = float(input("Nhập tọa độ x của điểm B: "))
yB = float(input("Nhập tọa độ y của điểm B: "))

# Tính và xuất độ dài đoạn AB
do_dai_AB = tinh_do_dai_AB(xA, yA, xB, yB)
print(f"Độ dài đoạn AB = {do_dai_AB:.2f}")
