'''
 Hàm oscillate
 Cho mã lệnh:
        for n in oscillate (-3,5):
            print(n, end =' ')
        print()

Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
-3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
'''
'''
Dưới đây là định nghĩa của hàm oscillate mà bạn yêu cầu. Hàm này sẽ tạo ra một trình lặp (generator) để giúp in ra dãy số theo thứ tự đã mô tả.
'''
def oscillate(start, end):
    # Tạo một dãy số từ start đến end
    for i in range(start, end + 1):
        yield i
        yield -i

# Kiểm tra hàm
for n in oscillate(-3, 5):
    print(n, end=' ')
print()

'''
Giải thích:
Hàm oscillate nhận hai tham số: start và end.
Sử dụng vòng lặp for để lặp từ start đến end.
Trong mỗi vòng lặp, hàm yield sẽ trả về giá trị i và sau đó là -i, tạo ra hiệu ứng "dao động".
Khi gọi hàm trong vòng lặp for, nó sẽ in ra các giá trị theo thứ tự như  yêu cầu.
'''