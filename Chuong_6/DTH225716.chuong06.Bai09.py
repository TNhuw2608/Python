'''
Xử lý mảng
Yêu cầu:
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố.
M[] ={3,6,7,8,11,17,2,90,2,5,4,5,8}
➔ 3, 7, 11,17, 5(2) ➔6 số lẻ
'''
def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def process_array(arr):
    """Xử lý mảng và in ra các thông tin theo yêu cầu."""
    odd_numbers = [num for num in arr if num % 2 != 0]
    even_numbers = [num for num in arr if num % 2 == 0]
    prime_numbers = [num for num in arr if is_prime(num)]
    non_prime_numbers = [num for num in arr if not is_prime(num) and num > 1]

    # Xuất ra kết quả
    print("Số lẻ:", ", ".join(map(str, odd_numbers)), f"({len(odd_numbers)} số lẻ)")
    print("Số chẵn:", ", ".join(map(str, even_numbers)), f"({len(even_numbers)} số chẵn)")
    print("Số nguyên tố:", ", ".join(map(str, prime_numbers)))
    print("Số không phải là số nguyên tố:", ", ".join(map(str, non_prime_numbers)))

# Dữ liệu đầu vào
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Gọi hàm để xử lý và in kết quả
process_array(M)