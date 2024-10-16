'''
Hàm kiểm tra số hoàn thiện, số thịnh vượng
Yêu cầu:
Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không?
(Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
Vd: 6 có các ước số là 1,2,3 và 6=1+2+3 ➔6 là số hoàn thiện)
b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number)hay
không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn
nó. Vd:12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 ➔12 là số thịnh vượng)
'''
def tong_uoc_so(n):
    if n < 1:
        return 0
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong

def kiem_tra_hoan_thien(n):
    if n <= 0:
        return False
    return tong_uoc_so(n) == n

def kiem_tra_thinh_vuong(n):
    if n <= 0:
        return False
    return tong_uoc_so(n) > n

# Kiểm tra các số
n = int(input("Nhập số nguyên dương n: "))

if kiem_tra_hoan_thien(n):
    print(f"{n} là số hoàn thiện.")
else:
    print(f"{n} không phải là số hoàn thiện.")

if kiem_tra_thinh_vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số thịnh vượng.")