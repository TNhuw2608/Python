'''
Viết chương trình tối ưu chuỗi
Yêu cầu:
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng
'''
def toi_uu_chuoi(s):
    # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi, sau đó thay thế nhiều khoảng trắng bằng một khoảng trắng
    return ' '.join(s.strip().split())

def main():
    print("Nhập một chuỗi:")
    s = input()
    chuoi_toi_uu = toi_uu_chuoi(s)
    print("Chuỗi tối ưu:", chuoi_toi_uu)

# Gọi hàm main để thực thi chương trình
main()


'''
def ToiUuChuoi(s):
 s2=s
 s2=s2.strip()
 arr=s2.split(' ')
 s2=""
 for x in arr:
 word=x
 if len(word.strip())!=0:
 s2=s2+word+" "
 return s2.strip()
s=" Trần Duy Thanh "
print(s,"=>",len(s))
s=ToiUuChuoi(s)
print(s,"=>",len(s))
'''