'''
Xử lý chuỗi với các hàm cơ bản
Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm

'''
def kiem_tra_chuoi(s):
    count_upper = sum(1 for c in s if c.isupper())  # Đếm chữ in hoa
    count_lower = sum(1 for c in s if c.islower())  # Đếm chữ in thường
    count_digit = sum(1 for c in s if c.isdigit())  # Đếm chữ số
    count_special = sum(1 for c in s if not c.isalnum() and not c.isspace())  # Đếm ký tự đặc biệt
    count_space = sum(1 for c in s if c.isspace())  # Đếm khoảng trắng

    # Đếm nguyên âm và phụ âm
    vowels = "aeiouAEIOU"
    count_vowel = sum(1 for c in s if c in vowels)  # Đếm nguyên âm
    count_consonant = sum(1 for c in s if c.isalpha() and c not in vowels)  # Đếm phụ âm

    # Xuất kết quả
    print(f"Số chữ in hoa: {count_upper}")
    print(f"Số chữ in thường: {count_lower}")
    print(f"Số chữ số: {count_digit}")
    print(f"Số ký tự đặc biệt: {count_special}")
    print(f"Số khoảng trắng: {count_space}")
    print(f"Số nguyên âm: {count_vowel}")
    print(f"Số phụ âm: {count_consonant}")

def main():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập vào một chuỗi: ")
    kiem_tra_chuoi(s)

# Gọi hàm main để thực thi chương trình
main()