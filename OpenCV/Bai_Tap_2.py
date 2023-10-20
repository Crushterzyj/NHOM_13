import cv2

# Đọc ảnh gốc
image = cv2.imread('image.jpg')
angle = float(input("Nhập góc xoay (độ): "))
height, width = image.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()