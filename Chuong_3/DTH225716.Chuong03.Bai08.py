def tinh_toan(a, b, phep_toan):
    if phep_toan == '+':
        return a + b
    elif phep_toan == '-':
        return a - b
    elif phep_toan == '*':
        return a * b
    elif phep_toan == '/':
        if b != 0:
            return a / b
        else:
            return "Không thể chia cho 0"
    else:
        return "Phép toán không hợp lệ"

# Nhập giá trị từ người dùng
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")

print("Kết quả:", tinh_toan(a, b, phep_toan))
