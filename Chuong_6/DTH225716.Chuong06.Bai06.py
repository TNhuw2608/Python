'''
 Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

'''
import random

def generate_unique_random_list(n, lower_bound=1, upper_bound=100):
    if n > (upper_bound - lower_bound + 1):
        raise ValueError("N quá lớn, không thể tạo số ngẫu nhiên không trùng nhau trong khoảng này.")
    
    unique_numbers = set()
    while len(unique_numbers) < n:
        num = random.randint(lower_bound, upper_bound)
        unique_numbers.add(num)
    
    return list(unique_numbers)

# Nhập số lượng N từ người dùng
try:
    N = int(input("Nhập vào số lượng số ngẫu nhiên (N): "))
    random_list = generate_unique_random_list(N)
    print("Danh sách số ngẫu nhiên không trùng nhau:", random_list)
except ValueError as e:
    print("Lỗi:", e)