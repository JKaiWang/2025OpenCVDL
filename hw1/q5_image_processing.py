import cv2

# ===== 5.1 Global Threshold =====
def global_threshold(image):
    if image is None:
        print("No Image!!")
        return 
    print("Running 5.1 Global Threshold...")

    # Step 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2. Apply global threshold
    _, threshold_image = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

    # Show result
    cv2.imshow("5.1 Global Threshold - Original", image)
    cv2.imshow("5.1 Global Threshold - Result", threshold_image)
    cv2.waitKey(1)


# ===== 5.2 Local (Adaptive) Threshold =====
def local_threshold(image):
    if image is None:
        print("No Image!!")
        return 
    print("Running 5.2 Local Threshold...")

    # Step 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2. Apply adaptive threshold
    threshold_image = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, -1
    )

    # Show result
    cv2.imshow("5.2 Local Threshold - Original", image)
    cv2.imshow("5.2 Local Threshold - Result", threshold_image)
    cv2.waitKey(1)
