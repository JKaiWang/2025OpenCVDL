import cv2
import numpy as np

def color_separation(image):
    if image is None:
        print("No image loaded")
        return 
    b, g, r = cv2.split(image)
    zeros = np.zeros_like(b)

    b_img = cv2.merge([b, zeros, zeros])
    g_img = cv2.merge([zeros, g, zeros])
    r_img = cv2.merge([zeros, zeros, r])

    cv2.imshow("B Channel", b_img)
    cv2.imshow("G Channel", g_img)
    cv2.imshow("R Channel", r_img)
    print("1.1 Color Separation done.")
    cv2.waitKey(1)
    return b, g, r


def color_transformation(image):
    if image is None:
        print("No image loaded.")
        return
    print("Running 1.2 Color Transformation...")

    # === Q1: 用 OpenCV 轉灰階 ===
    cv_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Q1 - cv_gray (cv2.cvtColor)", cv_gray)

    # === Q2: 自行平均灰階 ===
    b, g, r = cv2.split(image)
    avg_gray = ((b / 3) + (g / 3) + (r / 3)).astype(np.uint8)
    cv2.imshow("Q2 - avg_gray ((b+g+r)/3)", avg_gray)

    cv2.waitKey(1)  # 讓 OpenCV 視窗顯示出來
    print("1.2 Color Transformation done.")
