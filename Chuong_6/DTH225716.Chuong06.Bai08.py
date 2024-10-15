'''
Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp
dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.

'''
def input_float_list(n):
    """Nhập vào dãy n số thực."""
    while True:
        try:
            user_input = input(f"Nhập vào {n} số thực (cách nhau bởi dấu cách): ")
            numbers = list(map(float, user_input.split()))
            
            if len(numbers) != n:
                print(f"Vui lòng nhập đúng số lượng {n} số.")
                continue
            
            return numbers
        except ValueError:
            print("Vui lòng chỉ nhập các số thực, cách nhau bởi dấu cách.")

def main():
    # Nhập số lượng n từ người dùng
    while True:
        try:
            n = int(input("Nhập vào số lượng số thực (n): "))
            if n <= 0:
                print("Số lượng phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Nhập dãy số thực
    float_list = input_float_list(n)
    
    # Sắp xếp dãy số theo thứ tự giảm dần
    float_list.sort(reverse=True)
    
    # In ra dãy số đã sắp xếp
    print("Dãy số sau khi sắp xếp theo thứ tự giảm dần:", float_list)

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()