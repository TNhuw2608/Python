'''

 Trích lọc số âm trong chuỗi
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12
'''
import re

def NegativeNumberInStrings(s):
    # Sử dụng biểu thức chính quy để tìm các số âm
    negative_numbers = re.findall(r'-\d+', s)
    
    # Chuyển đổi các số âm từ chuỗi sang kiểu số nguyên
    negative_numbers = [int(num) for num in negative_numbers]
    
    # Xuất ra các số nguyên âm
    return negative_numbers

def main():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập vào một chuỗi: ")
    result = NegativeNumberInStrings(s)
    
    # In kết quả
    if result:
        print("Các số nguyên âm trong chuỗi là:", result)
    else:
        print("Không có số nguyên âm trong chuỗi.")

# Gọi hàm main để thực thi chương trình
main()