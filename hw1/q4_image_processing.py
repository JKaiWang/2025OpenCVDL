import cv2
import numpy as np

def transform_burger(image, rotation=0.0, scale=1.0, tx=0.0, ty=0.0, show=True):
    """
    Q4: Transforms 功能
    根據 rotation、scale、tx、ty 對影像進行旋轉、縮放和平移
    """
    if image is None:
        print("[ERROR] No image loaded!")
        return None

    print(f"Running 4. Transform... (Rotation={rotation}°, Scale={scale}, Tx={tx}, Ty={ty})")

    h, w = image.shape[:2]
    center = (240, 200)

    # 旋轉＋縮放矩陣
    M = cv2.getRotationMatrix2D(center, rotation, scale)
    # 加入平移
    M[0, 2] += tx
    M[1, 2] += ty

    # 仿射轉換
    transformed = cv2.warpAffine(image, M, (w, h))

    if show:
        cv2.imshow("Input Image", image)
        cv2.imshow("Output Image (Transformed)", transformed)
        cv2.waitKey(1)

    return transformed
