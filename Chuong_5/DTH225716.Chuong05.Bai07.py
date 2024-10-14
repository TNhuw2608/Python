'''
Tối ưu chuỗi danh từ
Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”
'''
def toi_uu_chuoi_danh_tu(s):
    # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi, sau đó thay thế nhiều khoảng trắng bằng một khoảng trắng
    optimized_string = ' '.join(s.strip().split())
    
    # Viết hoa ký tự đầu tiên của mỗi từ
    optimized_string = optimized_string.title()
    
    return optimized_string

def main():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập một chuỗi danh từ: ")
    chuoi_toi_uu = toi_uu_chuoi_danh_tu(s)
    
    # In kết quả
    print("Chuỗi tối ưu:", chuoi_toi_uu)

# Gọi hàm main để thực thi chương trình
main()