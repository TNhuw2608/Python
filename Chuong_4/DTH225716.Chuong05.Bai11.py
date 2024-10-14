'''
Kiểm tra kết quả thực hiện
Yêu cầu:
Cho 3 hàm dưới đây: 
def sum1(n):
 s = 0
 while n > 0:
 s += 1
 n -= 1
 return s
def sum2():
 global val
 s = 0
 while val > 0:
 s += 1
 val -= 1
 return s
def sum3():
 s = 0
 for i in range(val, 0, -1):
 s += 1
 return s                                                                                                                    
Hãy cho biết kết quả sau khi gọi các lệnh dưới đây:

Trường hợp 1:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum2())
 print(sum3())
main()

Trường hợp 2:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum3())
 print(sum2())
main()  

Trường hợp 3:
def main():
 global val
 val = 5
 print(sum2())
 print(sum1(5))
 print(sum3())
main()
'''


'''
Để kiểm tra kết quả thực hiện của các hàm và các trường hợp mà bạn đã cung cấp, chúng ta sẽ phân tích từng trường hợp.

### Các hàm đã cho:

1. sum1(n)
   - Hàm này nhận một tham số `n` và cộng dồn biến `s` từ 0 đến `n`, trả về giá trị `n`.
   - Kết quả của `sum1(n)` sẽ là `n`.

2. sum2()
   - Hàm này sử dụng biến toàn cục `val` và cộng dồn từ `val` đến 0, trả về giá trị của `val`.
   - Kết quả của `sum2()` sẽ là giá trị của `val`.

3. sum3()
   - Hàm này cũng sử dụng biến toàn cục `val` và sử dụng vòng lặp `for` để cộng dồn từ `val` đến 0, trả về giá trị của `val`.
   - Kết quả của `sum3()` cũng sẽ là giá trị của `val`.

### Trường hợp 1:

def main():
    global val
    val = 5
    print(sum1(5))  # Kết quả: 5
    print(sum2())   # Kết quả: 5
    print(sum3())   # Kết quả: 5

main()

**Kết quả**:
5
5
5

### Trường hợp 2:

def main():
    global val
    val = 5
    print(sum1(5))  # Kết quả: 5
    print(sum3())   # Kết quả: 5
    print(sum2())   # Kết quả: 5

main()

**Kết quả**:

5
5
5

### Trường hợp 3:

def main():
    global val
    val = 5
    print(sum2())   # Kết quả: 5
    print(sum1(5))  # Kết quả: 5
    print(sum3())   # Kết quả: 5

main()

**Kết quả**:

5
5
5

### Tóm tắt kết quả:
Trong tất cả ba trường hợp, khi gọi `main()`, kết quả in ra sẽ là:
```
5
5
5
```

Điều này xảy ra vì tất cả các hàm đều trả về giá trị của `val` hoặc `n` (đều là 5 trong trường hợp này).

'''