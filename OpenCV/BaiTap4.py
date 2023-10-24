import cv2
import numpy as np

def separate_image_with_thresholds(input_image, output_image, lower_threshold, upper_threshold):

    image = cv2.imread(input_image)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mask = cv2.inRange(gray_image, lower_threshold, upper_threshold)

    result_image = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow(output_image,result_image)
    cv2.waitKey()

input_image = "image.jpg"
output_image = "output_image.jpg"


threshold1=int(input("nguong 1 muon thay doi: "))
threshold2=int(input("nguong 2 muon thay doi: "))

separate_image_with_thresholds(input_image, output_image, threshold1, threshold2)
