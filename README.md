# 🚗 Number Plate Detection and OCR
## 🚀 Live Demo

👉 [Open Number Plate Detection & OCR App](https://number-plate-ocr.streamlit.app/)

A computer vision project that detects vehicle number plates using **YOLO** and extracts the plate text using **EasyOCR**. The project also includes a **Streamlit web application** where users can upload a video and process it automatically.

## 📌 Project Overview

This project combines object detection and Optical Character Recognition (OCR) to detect vehicle number plates from video.

The system performs the following steps:

**Video → YOLO Number Plate Detection → Plate Cropping → EasyOCR → Detected Text → Processed Video**

The trained YOLO model detects the number plate, while EasyOCR reads the text from the detected plate.

---

## ✨ Features

* 🚘 Number plate detection using YOLO
* 🔤 Number plate text recognition using EasyOCR
* 🎥 Video processing
* 🟩 Bounding boxes around detected plates
* 📝 Displays detected plate text on the video
* 📊 Processing progress indicator
* 🌐 Streamlit web interface
* ⬇️ Download processed video

---

## 🛠️ Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming language          |
| YOLO       | Number plate detection        |
| EasyOCR    | Optical Character Recognition |
| OpenCV     | Video and image processing    |
| Streamlit  | Web application               |
| PyTorch    | Deep learning framework       |

---

## 📂 Project Structure

```text
number-plate-detection-and-ocr/
│
├── app.py
├── best.pt
├── requirements.txt
├── README.md
├── .gitignore
│
└── .venv/
```

> `.venv` is used only for local development and should not be uploaded to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abdulwahaboffical210/number-plate-detection-and-ocr.git
```

### 2. Open the project folder

```bash
cd number-plate-detection-and-ocr
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 🖥️ How to Use

1. Open the Streamlit application.
2. Upload a vehicle video.
3. Click **Process Video**.
4. YOLO detects the number plates.
5. The detected plate area is cropped.
6. EasyOCR reads the text.
7. The detected plate and OCR text are displayed on the video.
8. Download the processed video.

---

## 🤖 YOLO Model

The project uses a custom-trained YOLO model stored in:

```text
best.pt
```

The model is responsible for detecting vehicle number plates in video frames.

---

## 🔤 OCR Pipeline

After detecting a number plate:

```text
Detected Plate
      ↓
Crop Plate Region
      ↓
EasyOCR
      ↓
Extract Text
      ↓
Display Text on Video
```

---

## 🎥 Output

The processed video contains:

* Number plate bounding boxes
* OCR-detected text
* Original video frames
* Processed output ready for download

---

## 📸 Screenshots

Screenshots of the Streamlit application can be added here.

Example:

```text
screenshots/
├── home.png
└── result.png
```

---

## 🚀 Future Improvements

* Improve OCR accuracy
* Add vehicle tracking
* Add unique tracking IDs
* Improve number plate image preprocessing
* Support multiple languages
* Store detected plate numbers in a database
* Add date and time for each detection
* Add CSV export of detected number plates
* Deploy the application online

---

## ⚠️ Limitations

OCR accuracy can depend on:

* Video quality
* Number plate size
* Lighting conditions
* Camera angle
* Motion blur
* Plate visibility
* OCR recognition quality

---

## 👨‍💻 Author

**Abdul Wahab**

Computer Science Student
Aspiring AI Engineer & Data Scientist

---

## 📚 Project Purpose

This project was developed as a computer vision and AI project to demonstrate the practical use of:

* Object Detection
* Computer Vision
* Deep Learning
* Optical Character Recognition
* Python
* Streamlit

---

## ⭐ If You Find This Project Useful

Feel free to explore the repository and learn from the implementation.
