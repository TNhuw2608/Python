'''
Viết chương trình tính căn bậc 2 lồng nhau
 NHập n. Tính S(n) căn (2+Căn(2+Căn(2+Căn(+...+Căn(2))))), n có dấu căn lòng nhau
'''
import math

def tinh_can_bac_2_long_nhau(n):
    # Bắt đầu với giá trị 2
    ket_qua = 2.0
    # Lặp n lần để tính căn bậc 2 lồng nhau
    for _ in range(n):
        ket_qua = math.sqrt(2 + ket_qua)
    return ket_qua

# Nhập số n từ bàn phím
n = int(input("Nhập số n (số dấu căn lồng nhau): "))

# Tính và xuất S(n)
if n < 0:
    print("Giá trị n phải không âm.")
else:
    S_n = tinh_can_bac_2_long_nhau(n)
    print(f"S({n}) = {S_n:.6f}")