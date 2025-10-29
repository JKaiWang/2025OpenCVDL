import cv2
import numpy as np


# =========================================================
# Helper Functions
# =========================================================

def _preprocess_gray_blur(image):
    """
    Convert input image to grayscale and apply 3x3 Gaussian blur.
    Returns blurred grayscale float32 image.
    """
    if image is None:
        print("[ERROR] Image is None.")
        return None

    # Convert to grayscale if needed
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (3, 3), 0).astype(np.float32)
    return blur


def _manual_conv3x3(img, kernel):
    """
    Perform manual 3x3 convolution with zero padding.
    """
    h, w = img.shape
    padded = np.zeros((h + 2, w + 2), dtype=np.float32)
    padded[1:-1, 1:-1] = img

    result = np.zeros_like(img, dtype=np.float32)

    for x in range(h):
        for y in range(w):
            region = padded[x:x+3, y:y+3]
            result[x, y] = np.sum(region * kernel)
    return result


# =========================================================
# 3.1 Sobel X
# =========================================================
def sobel_x(image, show=False):
    """
    Apply Sobel X operator manually to detect vertical edges.
    """
    if image is None:
        print("[ERROR] No image loaded for Sobel X.")
        return

    print("Running 3.1 Sobel X...")

    blur = _preprocess_gray_blur(image)
    if blur is None:
        return

    sobel_x_kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    gx = _manual_conv3x3(blur, sobel_x_kernel)

    if show:
        cv2.imshow("Sobel X (Vertical Edge)", cv2.convertScaleAbs(gx))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return gx


# =========================================================
# 3.2 Sobel Y
# =========================================================
def sobel_y(image, show=False):
    """
    Apply Sobel Y operator manually to detect horizontal edges.
    """
    if image is None:
        print("[ERROR] No image loaded for Sobel Y.")
        return

    print("Running 3.2 Sobel Y...")

    blur = _preprocess_gray_blur(image)
    if blur is None:
        return

    sobel_y_kernel = np.array([
        [1,  2,  1],
        [0,  0,  0],
        [-1, -2, -1]
    ], dtype=np.float32)

    gy = _manual_conv3x3(blur, sobel_y_kernel)

    if show:
        cv2.imshow("Sobel Y (Horizontal Edge)", cv2.convertScaleAbs(gy))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return gy


# =========================================================
# 3.3 Combination and Threshold
# =========================================================
def combination_and_threshold(image, show=True):
    """
    Combine Sobel X and Y results and apply two thresholds.
    """
    if image is None:
        print("[ERROR] No image loaded for Combination and Threshold.")
        return

    print("Running 3.3 Combination and Threshold...")

    gx = sobel_x(image, show=False)
    gy = sobel_y(image, show=False)

    if gx is None or gy is None:
        return

    # Gradient magnitude
    mag = np.sqrt(gx**2 + gy**2)
    normalized = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Apply thresholds
    _, th128 = cv2.threshold(normalized, 128, 255, cv2.THRESH_BINARY)
    _, th28 = cv2.threshold(normalized, 28, 255, cv2.THRESH_BINARY)

    if show:
        cv2.imshow("Combination (Sobel X + Sobel Y)", normalized)
        cv2.imshow("Threshold = 128", th128)
        cv2.imshow("Threshold = 28", th28)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return normalized


# =========================================================
# 3.4 Gradient Angle
# =========================================================
def gradient_angle(image, show=True):
    """
    Compute gradient angle and display two specific angle ranges:
      - 170°~190°
      - 260°~280°
    """
    if image is None:
        print("[ERROR] No image loaded for Gradient Angle.")
        return

    print("Running 3.4 Gradient Angle...")

    blur = _preprocess_gray_blur(image)
    if blur is None:
        return

    # Sobel kernels
    sobel_x_kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    sobel_y_kernel = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ], dtype=np.float32)

    gx = _manual_conv3x3(blur, sobel_x_kernel)
    gy = _manual_conv3x3(blur, sobel_y_kernel)

    magnitude = np.sqrt(gx**2 + gy**2)
    normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Compute gradient angle
    angle = np.degrees(np.arctan2(gy, gx))
    angle = (angle + 360) % 360

    # Create two masks
    mask1 = ((angle >= 170) & (angle <= 190)).astype(np.uint8) * 255
    mask2 = ((angle >= 260) & (angle <= 280)).astype(np.uint8) * 255

    # Apply bitwise AND
    result1 = cv2.bitwise_and(normalized, normalized, mask=mask1)
    result2 = cv2.bitwise_and(normalized, normalized, mask=mask2)

    if show:
        cv2.imshow("Angle Range [170, 190]", result1)
        cv2.imshow("Angle Range [260, 280]", result2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return result1, result2
