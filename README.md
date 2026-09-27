# 2025 OpenCVDL 作業紀錄

本專案整理 2025 OpenCVDL 課程的 Homework 1 與 Homework 2。內容著重於從傳統影像處理到深度學習影像分類的實作與資料準備。

## Homework 1：OpenCV 基礎影像處理

### 作業要求

Homework 1 依功能分為五個主題：

1. 色彩處理：Color Separation、Color Transformation、Color Extraction。
2. 影像平滑：Gaussian Blur、Bilateral Filter、Median Filter。
3. 邊緣偵測：Sobel X、Sobel Y、梯度合成與閾值化、指定梯度角度範圍。
4. 幾何轉換：旋轉、縮放與平移。
5. 二值化：Global Threshold 與 Local (Adaptive) Threshold。

### 我們做了什麼

- 以 PyQt5 建立圖形介面，支援載入兩張影像、操作各題功能、輸入幾何轉換參數，以及關閉 OpenCV 視窗。
- 實作 B、G、R 通道分離，並比較 OpenCV 灰階轉換和自行計算的 RGB 平均灰階。
- 以滑桿即時調整 Gaussian、Bilateral、Median Filter 的核心大小。
- 手動完成 3×3 Sobel 卷積與零補邊，輸出 X／Y 梯度、梯度幅值、不同閾值結果，以及指定梯度方向的遮罩結果。
- 完成旋轉、縮放、平移的仿射轉換，以及全域／局部二值化。

> 目前介面雖有 **1.3 Color Extraction** 按鈕，但程式尚未綁定事件或實作對應函式。

### 實作方法

| 功能 | 實作方式 |
| --- | --- |
| 色彩處理 | `cv2.split`、`cv2.merge` 分離 BGR 通道；`cv2.cvtColor` 與 `(B+G+R)/3` 產生灰階。 |
| 影像平滑 | 使用 `cv2.GaussianBlur`、`cv2.bilateralFilter`、`cv2.medianBlur`；核心大小以 `2m+1` 決定。 |
| 邊緣偵測 | 灰階化與 Gaussian blur 後，以 NumPy 手動卷積 Sobel kernel；用 `sqrt(Gx²+Gy²)` 求梯度幅值。 |
| 幾何轉換 | 使用 `cv2.getRotationMatrix2D` 建立旋轉縮放矩陣，加入 Tx、Ty 後以 `cv2.warpAffine` 輸出。 |
| 二值化 | 使用 `cv2.threshold` 做固定閾值二值化；使用 `cv2.adaptiveThreshold` 做局部自適應二值化。 |

### 獲得的技能與知識

- 熟悉 OpenCV 的 BGR 色彩順序、通道操作、灰階化與二值化。
- 理解各種濾波器在去雜訊、保留邊緣與細節上的差異。
- 掌握卷積、零補邊、Sobel 梯度、梯度幅值與方向的原理。
- 能使用仿射矩陣完成旋轉、縮放、平移等影像幾何轉換。
- 練習把 OpenCV 影像處理整合至 PyQt5 GUI，並提供互動式參數調整。

執行 HW1：

```bash
pip install opencv-python numpy PyQt5
cd hw1
python main.py
```

## Homework 2：影像分類測試與推論資料

### 作業要求

從保留的資料可辨識出兩個影像分類任務：

1. **Q1：手寫數字分類**：對 `hw2/Q1_TestData` 的 10 張 28×28 測試圖片進行預測。
2. **Q2：物件分類推論**：對 `hw2/Q2_inference_img` 的圖片進行類別預測；其中 10 張 32×32 圖片的檔名為 airplane、automobile、bird、cat、deer、dog、frog、horse、ship、truck，對應 CIFAR-10 的常見類別集合；另有一張 `chair.jpg` 作為額外推論圖片。

### 我們做了什麼

- 整理 Q1 的 `test_0.png` 至 `test_9.png`，作為手寫數字模型的測試輸入。
- 整理 Q2 的 11 張物件圖片，包含 CIFAR-10 十類物件及一張額外 chair 圖片，供模型逐張進行推論與驗證。
- 以 `Q1_TestData`、`Q2_inference_img` 分開保存兩題輸入，讓分類程式能依題目讀取對應資料。

### 實作方法

目前 `hw2` 只保留測試／推論圖片，未包含模型程式、權重、訓練設定或結果紀錄。因此可確認的實作為資料準備；完整分類流程應為：

1. 載入已訓練的分類模型。
2. 依模型規格前處理影像，例如灰階或 RGB 轉換、縮放、正規化與加入 batch 維度。
3. 執行前向推論，取得每個類別的分數或機率。
4. 選取最高分數的類別，輸出預測名稱與信心分數。

### 獲得的技能與知識

- 了解手寫數字分類與彩色物件分類在輸入尺寸及前處理上的差異。
- 理解分類模型在推論時必須沿用訓練階段的前處理方式。
- 熟悉多類別分類的輸出概念：比較各類別分數，選擇最高者作為預測結果。
- 建立將測試資料、推論圖片、程式、權重及結果紀錄妥善保存的可重現性觀念。

## 專案結構

```text
2025OpenCVDL/
├── hw1/                         # OpenCV 與 PyQt5 影像處理程式
│   ├── main.py
│   └── Dataset_OpenCvDl_Hw1/     # HW1 各題示範影像
└── hw2/
    ├── Q1_TestData/              # 28×28 手寫數字測試圖片
    └── Q2_inference_img/         # 物件分類推論圖片
```
