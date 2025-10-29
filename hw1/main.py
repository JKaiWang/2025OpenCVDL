from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGroupBox, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFileDialog
)
import cv2
import sys
import os
from load_image import load_image
from q1_image_processing import color_separation, color_transformation
from q2_image_processing import gaussian_filter, bilateral_filer, median_filter
from q3_image_processing import sobel_x, sobel_y, combination_and_threshold, gradient_angle
from q4_image_processing import transform_burger
from q5_image_processing import global_threshold, local_threshold

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hw1 - OpenCV & PyQt5 GUI")
        self.setGeometry(300, 100, 800, 700)
        self.img1 = None
        self.img2 = None
        self.path1 = ""
        self.path2 = ""
        self.setupUI()

    def setupUI(self):
        # ===== 左側 Load Buttons =====
        self.load_img1_btn = QPushButton("Load Image 1")
        self.load_img2_btn = QPushButton("Load Image 2")
        self.close_windows_btn = QPushButton("Close All Windows")  

        # 加上事件
        self.load_img1_btn.clicked.connect(self.load_image1)
        self.load_img2_btn.clicked.connect(self.load_image2)
        self.close_windows_btn.clicked.connect(self.close_opencv_windows)  

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.load_img1_btn)
        left_layout.addWidget(self.load_img2_btn)
        left_layout.addWidget(self.close_windows_btn)  

        # ===== Q1: Image Processing =====
        self.grp1 = QGroupBox("1. Image Processing")
        self.q1_btn1 = QPushButton("1.1 Color Separation")
        self.q1_btn2 = QPushButton("1.2 Color Transformation")
        self.q1_btn3 = QPushButton("1.3 Color Extraction")

        # 第一題功能
        self.q1_btn1.clicked.connect(lambda: color_separation(self.img1))
        self.q1_btn2.clicked.connect(lambda: color_transformation(self.img1))

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.q1_btn1)
        vbox1.addWidget(self.q1_btn2)
        vbox1.addWidget(self.q1_btn3)
        self.grp1.setLayout(vbox1)

        # ===== Q2: Image Smoothing =====
        self.grp2 = QGroupBox("2. Image Smoothing")
        self.q2_btn1 = QPushButton("2.1 Gaussian blur")
        self.q2_btn2 = QPushButton("2.2 Bilateral filter")
        self.q2_btn3 = QPushButton("2.3 Median filter")

    
        self.q2_btn1.clicked.connect(lambda: gaussian_filter(self.img1))
        self.q2_btn2.clicked.connect(lambda: bilateral_filer(self.img1))
        self.q2_btn3.clicked.connect(lambda: median_filter(self.img2))

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.q2_btn1)
        vbox2.addWidget(self.q2_btn2)
        vbox2.addWidget(self.q2_btn3)
        self.grp2.setLayout(vbox2)

        # ===== Q3: Edge Detection =====
        self.grp3 = QGroupBox("3. Edge Detection")
        self.q3_btn1 = QPushButton("3.1 Sobel X")
        self.q3_btn2 = QPushButton("3.2 Sobel Y")
        self.q3_btn3 = QPushButton("3.3 Combination and Threshold")
        self.q3_btn4 = QPushButton("3.4 Gradient Angle")

        self.q3_btn1.clicked.connect(lambda: sobel_x(self.img1, show=True))
        self.q3_btn2.clicked.connect(lambda: sobel_y(self.img1, show=True))
        self.q3_btn3.clicked.connect(lambda: combination_and_threshold(self.img1))
        self.q3_btn4.clicked.connect(lambda: gradient_angle(self.img1))

        vbox3 = QVBoxLayout()
        for b in [self.q3_btn1, self.q3_btn2, self.q3_btn3, self.q3_btn4]:
            vbox3.addWidget(b)
        self.grp3.setLayout(vbox3)

        # ===== Q4: Transforms =====
        self.grp4 = QGroupBox("4. Transforms")
        self.label_rot = QLabel("Rotation:")
        self.label_scale = QLabel("Scaling:")
        self.label_tx = QLabel("Tx:")
        self.label_ty = QLabel("Ty:")
        self.input_rot = QLineEdit()
        self.input_scale = QLineEdit()
        self.input_tx = QLineEdit()
        self.input_ty = QLineEdit()
        self.btn_transform = QPushButton("4. Transforms")

        self.btn_transform.clicked.connect(self.run_transform)

        grid4 = QGridLayout()
        grid4.addWidget(self.label_rot, 0, 0)
        grid4.addWidget(self.input_rot, 0, 1)
        grid4.addWidget(QLabel("deg"), 0, 2)
        grid4.addWidget(self.label_scale, 1, 0)
        grid4.addWidget(self.input_scale, 1, 1)
        grid4.addWidget(QLabel(""), 1, 2)
        grid4.addWidget(self.label_tx, 2, 0)
        grid4.addWidget(self.input_tx, 2, 1)
        grid4.addWidget(QLabel("pixel"), 2, 2)
        grid4.addWidget(self.label_ty, 3, 0)
        grid4.addWidget(self.input_ty, 3, 1)
        grid4.addWidget(QLabel("pixel"), 3, 2)
        grid4.addWidget(self.btn_transform, 4, 0, 1, 3)
        self.grp4.setLayout(grid4)

        # ===== Q5: Adaptive Threshold =====
        self.grp5 = QGroupBox("5. Adaptive Threshold")
        self.q5_btn1 = QPushButton("5.1 Global Threshold")
        self.q5_btn2 = QPushButton("5.2 Local Threshold")
        
        self.q5_btn1.clicked.connect(lambda: global_threshold(self.img1))
        self.q5_btn2.clicked.connect(lambda: local_threshold(self.img1))


        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.q5_btn1)
        vbox5.addWidget(self.q5_btn2)
        self.grp5.setLayout(vbox5)

        # ===== Main Layout =====
        grid = QGridLayout()
        grid.addWidget(self.grp1, 0, 1)
        grid.addWidget(self.grp2, 1, 1)
        grid.addWidget(self.grp3, 2, 1)
        grid.addLayout(left_layout, 1, 0)
        grid.addWidget(self.grp4, 0, 2)
        grid.addWidget(self.grp5, 1, 2)

        self.setLayout(grid)

    # ====== 圖片載入 ======
    def load_image1(self):
        self.img1, self.path1 = load_image(self, "Select Image 1")

    def load_image2(self):
        self.img2, self.path2 = load_image(self, "Select Image 2")

    # ====== 關閉 OpenCV 假視窗 ======
    def close_opencv_windows(self):
        cv2.destroyAllWindows()
        print("All OpenCV windows closed.")
    def run_transform(self):
        if self.img1 is None:
            print("No Image loaded!")
            return 
        try:
            rotation = float(self.input_rot.text() or 0)
            scale = float(self.input_scale.text() or 1)
            tx = float(self.input_tx.text() or 0)
            ty = float(self.input_ty.text() or 0)
        except ValueError:
            print("Invalid input!")
            return 
        transform_burger(self.img1 , rotation , scale , tx , ty , show= True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
