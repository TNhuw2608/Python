'''
code python Vẽ hình dùng Sleep                                                                                           , 
            *
          * *
        * * * 
* * * * * * *
* * *
* *
* 
'''


import turtle
import time

def ve_hinh_vuong(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        time.sleep(0.5)  # Dừng 0.5 giây giữa các bước

# Thiết lập cửa sổ vẽ
turtle.title("Vẽ Hình Vuông")
turtle.speed(1)  # Tốc độ vẽ

# Vẽ hình vuông với kích thước 100
ve_hinh_vuong(100)

# Kết thúc vẽ
turtle.done()