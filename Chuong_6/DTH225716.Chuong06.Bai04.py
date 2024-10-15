'''
Xác định kết quả khi thực thi list
Yêu cầu:
Cho list
lst = [3, 0, 1, 5, 2]
x = 2
Hãy cho biết kết quả:
(a) lst[0]?
(b) lst[3]?
(c) lst[x]?
(d) lst[-x]?
(e) lst[x + 1]?
(f) lst[x] + 1?
(g) lst[lst[x]]?
(h) lst[lst[lst[x]]]?

'''
'''
Kết quả từng yêu cầu:
(a) lst[0]
Kết quả: 3
Giải thích: Phần tử đầu tiên của danh sách là 3.

(b) lst[3]
Kết quả: 5
Giải thích: Phần tử tại chỉ số 3 là 5.

(c) lst[x]
Kết quả: 1
Giải thích: lst[2] (vì x = 2) có giá trị là 1.

(d) lst[-x]
Kết quả: 1
Giải thích: lst[-2] truy cập phần tử từ cuối danh sách, có giá trị là 1.

(e) lst[x + 1]
Kết quả: 5
Giải thích: lst[3] (vì x + 1 = 3) có giá trị là 5.

(f) lst[x] + 1
Kết quả: 2
Giải thích: lst[2] có giá trị 1, do đó 1 + 1 = 2.

(g) lst[lst[x]]
Kết quả: 5
Giải thích: lst[x] là 1, nên lst[1] có giá trị là 0.

(h) lst[lst[lst[x]]]
Kết quả: 2
Giải thích:
lst[x] là 1,
lst[lst[x]] là lst[1] (có giá trị 0),
lst[lst[lst[x]]] là lst[0] (có giá trị 3),
Cuối cùng, lst[0] là 3, nhưng do có sự nhầm lẫn, ta xem lại:
Thực tế, lst[lst[lst[x]]] = lst[lst[1]] = lst[0] = 3.
Tóm lại, kết quả cho từng yêu cầu là:

(a) 3
(b) 5
(c) 1
(d) 1
(e) 5
(f) 2
(g) 0
(h) 3
'''