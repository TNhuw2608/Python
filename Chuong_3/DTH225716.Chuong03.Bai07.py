from datetime import datetime, timedelta

def ngay_ke_sau(ngay, thang, nam):
    try:
        # Tạo đối tượng ngày
        date_input = datetime(nam, thang, ngay)
        # Tính ngày kế sau
        date_ke_sau = date_input + timedelta(days=1)
        return date_ke_sau.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ"

# Nhập ngày từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print("Ngày kế sau là:", ngay_ke_sau(ngay, thang, nam))