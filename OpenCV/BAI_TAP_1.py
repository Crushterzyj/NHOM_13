# ###cho phep nhap (x,y) de zoom in/out 1 anh. hien thi anh ban
# ###dau va anh sau khi zoom

import cv2

# Đọc hình ảnh gốc
image = cv2.imread('image.jpg')

# Nhập tỷ lệ (x, y) cho việc zoom in/out0
x_scale = float(input("Nhập tỉ lệ theo trục X: "))
y_scale = float(input("Nhập tỉ lệ theo trục Y: "))

# Thực hiện zoom in/out
zoomed_image = cv2.resize(image, None, fx=x_scale, fy=y_scale)

# Hiển thị ảnh sau khi zoom
cv2.imshow('Image', image)
cv2.imshow('Zoomed Image', zoomed_image)

cv2.waitKey()