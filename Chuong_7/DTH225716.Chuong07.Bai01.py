'''
Quản lý Sản phẩm- Text File
Yêu cầu:
Viết chương trình nhập vào thông tin của một sản phẩm:
Mã: Chuỗi
Tên: Chuỗi
Đơn Giá: Số
Mỗi một Sản phẩm sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
MSSP;Tên Sản phẩm; Đơn giá
Mẫu Dữ liệu lưu nối đuôi vào file tương tự như dưới đây:
sv1;Cocacolala;15.5
sp2;Bưởi 5 Roi;18.0
sp3;Bia 333;14.5
Sau đó thực hiện 2 chức năng chính:
a) xuất danh sách sản phẩm từ File
b) Sắp xếp Sản phẩm theo đơn giá giảm dần
'''
'''
#Bước 1: Tạo 1 Python XuLyFile.py :
def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()
def DocFile(path):
    arrProduct=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct
#Bước 2: Tạo 1 file TestLuuFile.py:
from XuLyFile import *
masp=input("nhập mã SP:")
tensp=input("nhập tên sp:")
dongia=float(input("nhập giá:"))
line=masp+";"+tensp+";"+str(dongia)

LuuFile("database.txt",line)

#Bước 3: Tạo 1 file TestDocFile.py:
from XuLyFile import *
dssp=DocFile("database.txt")
#print(dssp)
def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element,end='\t')
        print()
    print()
XuatSanPham(dssp)
def SortSp(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a=dssp[i]
            b=dssp[j]
            if a[2]>b[2]:
                dssp[i]=b
                dssp[j]=a
SortSp(dssp)
print("Sản phẩm sau khi sắp xếp giá:")
XuatSanPham(dssp)
'''
import os

def input_product():
    """Nhập thông tin sản phẩm từ người dùng."""
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập đơn giá sản phẩm: "))
    return (code, name, price)

def save_product_to_file(product, filename="products.txt"):
    """Lưu thông tin sản phẩm vào file."""
    with open(filename, "a") as file:
        file.write(f"{product[0]};{product[1]};{product[2]:.2f}\n")

def load_products_from_file(filename="products.txt"):
    """Tải danh sách sản phẩm từ file."""
    products = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 3:
                    code = parts[0]
                    name = parts[1]
                    price = float(parts[2])
                    products.append((code, name, price))
    return products

def display_products(products):
    """Hiển thị danh sách sản phẩm."""
    if not products:
        print("Không có sản phẩm nào.")
        return

    print("\nDanh sách sản phẩm:")
    for product in products:
        print(f"Mã: {product[0]}, Tên: {product[1]}, Đơn giá: {product[2]:.2f}")

def sort_products_by_price(products):
    """Sắp xếp sản phẩm theo đơn giá giảm dần."""
    return sorted(products, key=lambda x: x[2], reverse=True)

def main():
    while True:
        print("\nChương trình quản lý sản phẩm")
        print("1. Nhập sản phẩm")
        print("2. Xuất danh sách sản phẩm")
        print("3. Sắp xếp sản phẩm theo đơn giá giảm dần")
        print("4. Thoát")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1':
            product = input_product()
            save_product_to_file(product)
            print("Sản phẩm đã được lưu.")
        elif choice == '2':
            products = load_products_from_file()
            display_products(products)
        elif choice == '3':
            products = load_products_from_file()
            sorted_products = sort_products_by_price(products)
            display_products(sorted_products)
        elif choice == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()