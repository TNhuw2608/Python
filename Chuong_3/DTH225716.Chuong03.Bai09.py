def quy_cua_thang(thang):
    if thang in [1, 2, 3]:
        return "Quý 1"
    elif thang in [4, 5, 6]:
        return "Quý 2"
    elif thang in [7, 8, 9]:
        return "Quý 3"
    elif thang in [10, 11, 12]:
        return "Quý 4"
    else:
        return "Tháng không hợp lệ"

# Nhập tháng từ người dùng
thang = int(input("Nhập tháng: "))
print("Tháng", thang, "thuộc", quy_cua_thang(thang))