'''
Các hàm quan trọng trong xử lý chuỗi của Python

Yêu cầu:
Trình bày một số hàm quan trọng trong xử lý Chuỗi của Python
'''


'''


1. len()
- Mô tả: Trả về độ dài của chuỗi.
- Ví dụ: 
  s = "Hello"
  print(len(s))  # Kết quả: 5
 

2. str.lower()
- Mô tả: Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường.
- Ví dụ: 
  s = "Hello World"
  print(s.lower())  # Kết quả: "hello world"
  

3. str.upper()
- Mô tả: Chuyển đổi tất cả các ký tự trong chuỗi thành chữ hoa.
- Ví dụ:
  s = "Hello World"
  print(s.upper())  # Kết quả: "HELLO WORLD"
  

4. `str.strip()`
- Mô tả: Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
- Ví dụ: 
 
  s = "   Hello   "
  print(s.strip())  # Kết quả: "Hello"
 

5. `str.split(separator)`
- Mô tả**: Tách chuỗi thành danh sách các chuỗi con dựa trên ký tự phân tách.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.split())  # Kết quả: ['Hello', 'World']
  ```

### 6. `str.join(iterable)`
- **Mô tả**: Nối các chuỗi trong một iterable (như danh sách) thành một chuỗi, sử dụng chuỗi gọi hàm làm ký tự phân tách.
- **Ví dụ**: 
  ```python
  words = ['Hello', 'World']
  print(' '.join(words))  # Kết quả: "Hello World"
  ```

### 7. `str.replace(old, new)`
- **Mô tả**: Thay thế tất cả các ký tự con `old` trong chuỗi bằng `new`.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.replace("World", "Python"))  # Kết quả: "Hello Python"
  ```

### 8. `str.find(sub)`
- **Mô tả**: Tìm vị trí đầu tiên của chuỗi con `sub` trong chuỗi. Nếu không tìm thấy, trả về -1.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.find("World"))  # Kết quả: 6
  ```

### 9. `str.startswith(prefix)`
- **Mô tả**: Kiểm tra xem chuỗi có bắt đầu bằng `prefix` hay không.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.startswith("Hello"))  # Kết quả: True
  ```

### 10. `str.endswith(suffix)`
- **Mô tả**: Kiểm tra xem chuỗi có kết thúc bằng `suffix` hay không.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.endswith("World"))  # Kết quả: True
  ```

### 11. `str.count(sub)`
- **Mô tả**: Đếm số lần xuất hiện của chuỗi con `sub` trong chuỗi.
- **Ví dụ**: 
  ```python
  s = "Hello World"
  print(s.count("o"))  # Kết quả: 2
  ```

### 12. `str.capitalize()`
- **Mô tả**: Chuyển đổi ký tự đầu tiên của chuỗi thành chữ hoa và các ký tự còn lại thành chữ thường.
- **Ví dụ**: 
  ```python
  s = "hello world"
  print(s.capitalize())  # Kết quả: "Hello world"
  ```

### 13. `str.title()`
- **Mô tả**: Chuyển đổi ký tự đầu tiên của mỗi từ thành chữ hoa.
- **Ví dụ**: 
  ```python
  s = "hello world"
  print(s.title())  # Kết quả: "Hello World"
  ```

### Tóm tắt
Python cung cấp nhiều phương thức phong phú để xử lý chuỗi, giúp lập trình viên dễ dàng làm việc với văn bản. Những hàm này cho phép thực hiện các thao tác phổ biến như tách, nối, tìm kiếm và thay thế trong chuỗi.
'''