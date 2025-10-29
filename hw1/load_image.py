# load_image.py
import cv2
from PyQt5.QtWidgets import QFileDialog
import os

def load_image(widget, title="Select Image"):
    dialog = QFileDialog(widget)
    dialog.setOptions(QFileDialog.DontUseNativeDialog)
    file_name, _ = dialog.getOpenFileName(
        widget, title, "", "Images (*.png *.jpg *.jpeg *.bmp)"
    )

    if file_name and os.path.exists(file_name):
        img = cv2.imread(file_name)
        if img is not None:
            print(f"Loaded image: {file_name}")
            return img, file_name
        else:
            print("Failed to read image file.")
            return None, ""
    else:
        print("No file selected or invalid path.")
        return None, ""
