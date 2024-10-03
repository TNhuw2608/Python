'''
Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python?

SyntaxError: Xảy ra khi có lỗi cú pháp trong mã, ví dụ như thiếu dấu ngoặc, dấu hai chấm, v.v.
Ví dụ:
print("Hello World"  # Thiếu dấu ngoặc đóng


TypeError:Xảy ra khi bạn thực hiện một phép toán không hợp lệ với kiểu dữ liệu.
Ví dụ:
result = "Hello" + 5  # Không thể cộng chuỗi và số


ValueError: Xảy ra khi một hàm nhận loại đối số đúng nhưng có giá trị không hợp lệ.
Ví dụ:
number = int("abc")  # Không thể chuyển đổi chuỗi không phải số


IndexError: Xảy ra khi bạn cố gắng truy cập một chỉ số không hợp lệ trong danh sách hoặc chuỗi.
Ví dụ:
my_list = [1, 2, 3]
print(my_list[5])  # Chỉ số 5 không tồn tại


KeyError: Xảy ra khi bạn cố gắng truy cập một khóa không tồn tại trong từ điển.
Ví dụ:
pythonmy_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # Khóa 'c' không tồn tại



FileNotFoundError:Xảy ra khi cố gắng mở một tệp không tồn tại.
Ví dụ:
with open('file.txt', 'r') as f:  # Tệp file.txt không tồn tại
    content = f.read()



'''