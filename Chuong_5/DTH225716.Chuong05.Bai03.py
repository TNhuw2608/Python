'''
 Xử lý Tách chuỗi
Yêu cầu:
Cho 1 Chuỗi như sau “5;7;8;-2;8;11;13;9;10” (có thể nhập bất kỳ từ bàn phím)
- xuất các chữ số trên các dòng riêng biệt
- Xuất có bao nhiêu chữ số chẵn
- Xuất có bao nhiêu số âm
- Xuất có bao nhiêu chữ số nguyên tố
- Tính giá trị trung bình
'''

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def xu_ly_chuoi(s):
    # Tách chuỗi thành danh sách số
    numbers = list(map(int, s.split(';')))
    
    # Xuất các số trên các dòng riêng biệt
    print("Các số:")
    for number in numbers:
        print(number)

    # Đếm số chẵn
    count_even = sum(1 for number in numbers if number % 2 == 0)
    print(f"Số chữ số chẵn: {count_even}")

    # Đếm số âm
    count_negative = sum(1 for number in numbers if number < 0)
    print(f"Số chữ số âm: {count_negative}")

    # Đếm số nguyên tố
    count_prime = sum(1 for number in numbers if is_prime(number))
    print(f"Số chữ số nguyên tố: {count_prime}")

    # Tính giá trị trung bình
    average = sum(numbers) / len(numbers) if numbers else 0
    print(f"Giá trị trung bình: {average:.2f}")

def main():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập chuỗi các số (cách nhau bằng ';'): ")
    xu_ly_chuoi(s)

# Gọi hàm main để thực thi chương trình
main()

'''

def CheckPrime(x):
 dem=0
 for i in range(1,x+1):
 if x % i ==0:
 dem+=1
 return dem==2
s="5;7;8;-2;8;11;-13;9;10"
arr=s.split(';')
sochan=0
soam=0
sont=0
sum=0
for x in arr:
 print(x)
 number=int(x)
 if number % 2 ==0:
 sochan+=1
 if number <0:
 soam+=1
 if CheckPrime(number):
 sont+=1
 sum=sum+number
print("Số chẵn =",sochan)
print("Số âm =",soam)
print("Số Nguyên tố =",sont)
print("Trung bình=",sum/len(arr))
'''