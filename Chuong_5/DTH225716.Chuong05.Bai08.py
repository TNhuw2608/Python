'''

Tách lấy tên bài hát
Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.
'''
import os

def lay_ten_file(duong_dan):
    """Lấy tên file bao gồm đuôi."""
    return os.path.basename(duong_dan)

def lay_ten_bai_hat(duong_dan):
    """Lấy tên file không có đuôi."""
    return os.path.splitext(os.path.basename(duong_dan))[0]

def main():
    # Nhập đường dẫn file nhạc từ bàn phím
    duong_dan = input("Nhập đường dẫn file nhạc: ")
    
    # Lấy tên file và tên bài hát
    ten_file = lay_ten_file(duong_dan)
    ten_bai_hat = lay_ten_bai_hat(duong_dan)
    
    # In kết quả
    print("Tên file:", ten_file)
    print("Tên bài hát:", ten_bai_hat)

# Gọi hàm main để thực thi chương trình
main()