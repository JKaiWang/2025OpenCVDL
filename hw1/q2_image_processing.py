import cv2
import numpy as np

def gaussian_filter(image):
    if image is None:
        print("No Image!!")
        return 
    print("Running 2.1 Gaussian Blurrrrr....")

    # === callback ===
    def on_trackbar(val):
        m = max(0, val)
        ksize = 2 * m + 1
        blur = cv2.GaussianBlur(image, (ksize, ksize), 0)
        cv2.imshow("2.1 Gaussian Blur", blur)

    # === 設定視窗與 trackbar ===
    cv2.namedWindow("2.1 Gaussian Blur", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("m", "2.1 Gaussian Blur", 1, 5, on_trackbar)
    on_trackbar(0)
    print("Tracker bar ready")

    # ✅ 關鍵：非阻塞顯示（不影響 PyQt 主程式）
    cv2.waitKey(1)
def bilateral_filer(image):
    if image is None:
        print("No Image")
        return
    print("Running 2.2 Bilateral Filter...")
    
    def on_trackbar(val):
        m = max(0 , val)
        d = 2*m +1
        sigmaColor = 90
        sigmaSpace = 90
        blur = cv2.bilateralFilter(image , d , sigmaColor , sigmaSpace)
        cv2.imshow("2.2 Bilateral Filter" , blur)
        print(f"Updated Bilarteral Filter (m = {m}) , kernel = {d}x{d}")

    cv2.namedWindow("2.2 Bilateral Filter" , cv2.WINDOW_NORMAL)
    cv2.createTrackbar("m" , "2.2 Bilateral Filter", 0 , 5 , on_trackbar)

    cv2.setTrackbarPos("m" , "2.2 Bilateral Filter" , 5)
    on_trackbar(5)

    print("Tracker bar ready")
    cv2.waitKey(1)
def median_filter(image):
    name = "2.3 Median Filter"
    if image is None:
        print("No Image")
        return
    print("Running 2.3 median filter")
    def on_trackbar(val):
        m= max(0, val)
        ksize = 2*m +1
        blur = cv2.medianBlur(image , ksize)
        cv2.imshow(name , blur)
        print(f"Updated Medain Filter m = {m} , kernel = {ksize}x{ksize}")

    cv2.namedWindow(name , cv2.WINDOW_NORMAL)
    cv2.createTrackbar("m", name , 0 , 5 , on_trackbar)

    cv2.setTrackbarPos("m" , name , 5)
    on_trackbar(5)

    print("Tracker bar ready")
    cv2.waitKey(1)
        