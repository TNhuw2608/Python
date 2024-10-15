'''
 Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai
quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong
'''
def is_sorted_increasing(lst):
    """Kiểm tra xem danh sách có được sắp xếp theo thứ tự tăng hay không."""
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def input_sorted_list():
    """Nhập vào dãy số theo thứ tự tăng."""
    while True:
        try:
            user_input = input("Nhập vào dãy số (cách nhau bởi dấu cách): ")
            # Chia chuỗi thành danh sách và chuyển đổi thành số nguyên
            numbers = list(map(int, user_input.split()))
            
            # Kiểm tra nếu dãy số được sắp xếp theo thứ tự tăng
            if is_sorted_increasing(numbers):
                return numbers
            else:
                print("Dãy số không theo thứ tự tăng, vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng chỉ nhập các số nguyên, cách nhau bởi dấu cách.")

# Gọi hàm để nhập dãy số
sorted_list = input_sorted_list()
print("Dãy số đã nhập theo thứ tự tăng:", sorted_list)