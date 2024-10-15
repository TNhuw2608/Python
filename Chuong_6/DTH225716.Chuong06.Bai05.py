'''
Xác định kết quả khi thực thi list
Yêu cầu:
Cho list
lst = [20, 1, -34, 40, -8, 60, 1, 3]
Hãy cho biết kết quả:
(a) lst
(b) lst[0:3]
(c) lst[4:8]
(d) lst[4:33]
(e) lst[-5:-3]
(f) lst[-22:3]
(g) lst[4:]
(h) lst[:]
(i) lst[:4]
(j) lst[1:5]
(k) -34 in lst
(l) -34 not in lst
(m) len(lst)
'''

'''
(a) lst
Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]
Giải thích: Đây là danh sách ban đầu.

(b) lst[0:3]
Kết quả: [20, 1, -34]
Giải thích: Truy cập từ chỉ số 0 đến chỉ số 2.

(c) lst[4:8]
Kết quả: [-8, 60, 1, 3]
Giải thích: Truy cập từ chỉ số 4 đến chỉ số 7.

(d) lst[4:33]
Kết quả: [-8, 60, 1, 3]
Giải thích: Truy cập từ chỉ số 4 đến cuối danh sách (chỉ số 33 vượt quá độ dài).

(e) lst[-5:-3]
Kết quả: [40, -8]
Giải thích: Truy cập từ chỉ số -5 đến chỉ số -4.

(f) lst[-22:3]
Kết quả: []
Giải thích: Chỉ số -22 vượt quá độ dài của danh sách, nên không có giá trị nào.

(g) lst[4:]
Kết quả: [-8, 60, 1, 3]
Giải thích: Truy cập từ chỉ số 4 đến cuối danh sách.

(h) lst[:]
Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]
Giải thích: Sao chép toàn bộ danh sách.

(i) lst[:4]
Kết quả: [20, 1, -34, 40]
Giải thích: Truy cập từ chỉ số 0 đến chỉ số 3.

(j) lst[1:5]
Kết quả: [1, -34, 40, -8]
Giải thích: Truy cập từ chỉ số 1 đến chỉ số 4.

(k) -34 in lst
Kết quả: True
Giải thích: Giá trị -34 có trong danh sách.

(l) -34 not in lst
Kết quả: False
Giải thích: Giá trị -34 không phải là không có trong danh sách.

(m) len(lst)
Kết quả: 8
Giải thích: Độ dài của danh sách là 8.

Tóm tắt kết quả:
(a) [20, 1, -34, 40, -8, 60, 1, 3]
(b) [20, 1, -34]
(c) [-8, 60, 1, 3]
(d) [-8, 60, 1, 3]
(e) [40, -8]
(f) []
(g) [-8, 60, 1, 3]
(h) [20, 1, -34, 40, -8, 60, 1, 3]
(i) [20, 1, -34, 40]
(j) [1, -34, 40, -8]
(k) True
(l) False
(m) 8
'''