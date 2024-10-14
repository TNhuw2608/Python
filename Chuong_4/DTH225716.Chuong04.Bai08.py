'''
 Viết chương trình tính loga(x)   Viết chương trình tính log a(x )
 với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a!= 1.( dùng loga(x)=lnx/lna)
'''



import math

def tinh_log_a_x(a, x):
    # Tính log_a(x)
    log_a_x = math.log(x) / math.log(a)
    return log_a_x

# Nhập các giá trị a và x từ bàn phím
a = float(input("Nhập giá trị a (a > 0 và a != 1): "))
x = float(input("Nhập giá trị x (x > 0): "))

# Kiểm tra điều kiện
if a <= 0 or a == 1:
    print("Giá trị a phải lớn hơn 0 và khác 1.")
elif x <= 0:
    print("Giá trị x phải lớn hơn 0.")
else:
    # Tính và xuất log_a(x)
    log_a_x = tinh_log_a_x(a, x)
    print(f"log_{a}({x}) = {log_a_x:.4f}")