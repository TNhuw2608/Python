def tinh_S(x, n):
    S = 0.0
    for i in range(n + 1):
        mu = 2 * i + 1  # Lũy thừa của x
        giai_thua = 1   # Tính giai thừa
        for j in range(1, mu + 1):
            giai_thua *= j
        S += (x ** mu) / giai_thua  # Cộng vào S
    return S

# Nhập giá trị từ người dùng
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

# Tính và in kết quả
ket_qua = tinh_S(x, n)
print("Giá trị của S(x, n) là:", ket_qua)