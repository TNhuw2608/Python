'''
Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím?

1. Sử dụng hàm input()
Hàm input() cho phép bạn nhận dữ liệu từ người dùng dưới dạng chuỗi. Bạn có thể cung cấp một thông điệp để hướng dẫn người dùng.

name = input("Nhập tên của bạn: ")
print("Xin chào, " + name + "!")


2. Chuyển đổi kiểu dữ liệu
Dữ liệu nhập vào từ hàm input() luôn là chuỗi. Nếu bạn cần số nguyên hoặc số thực, bạn phải chuyển đổi chúng.

Số nguyên:
age = int(input("Nhập tuổi của bạn: "))
Số thực:
height = float(input("Nhập chiều cao của bạn (m): "))


3. Nhập nhiều giá trị
Bạn có thể nhập nhiều giá trị cùng lúc bằng cách sử dụng phương pháp tách chuỗi.
values = input("Nhập ba số cách nhau bằng dấu cách: ").split()
a, b, c = map(int, values)  # Chuyển đổi sang số nguyên


4. Sử dụng sys.stdin để nhập dữ liệu
Bạn có thể sử dụng sys.stdin để nhập dữ liệu, đặc biệt hữu ích khi làm việc với nhiều dòng.
import sys

print("Nhập dữ liệu (Ctrl+D để kết thúc):")
data = sys.stdin.read()
print("Dữ liệu bạn đã nhập là:")
print(data)


5. Nhập dữ liệu từ file (nếu cần)
Nếu bạn muốn nhập dữ liệu từ một tệp, bạn có thể sử dụng hàm open() để đọc từ file.
with open('input.txt', 'r') as file:
    data = file.read()
print(data)


Tóm tắt
input(): Nhập dữ liệu từ bàn phím.
Chuyển đổi kiểu: Sử dụng int() hoặc float() để chuyển đổi.
Nhập nhiều giá trị: Sử dụng split() và map().
sys.stdin: Nhập dữ liệu từ nhiều dòng.
Đọc từ file: Sử dụng open() để đọc dữ liệu từ tệp.

'''