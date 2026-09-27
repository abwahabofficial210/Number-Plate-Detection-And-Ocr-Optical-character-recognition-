import streamlit as st
import cv2
import os
import tempfile
import easyocr
from ultralytics import YOLO

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="Number Plate Detection & OCR",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Number Plate Detection & OCR")
st.write(
    "Upload a video and detect number plates with YOLO "
    "and read the plate text using EasyOCR."
)

# -----------------------------
# LOAD MODEL
# -----------------------------

@st.cache_resource
def load_model():
    return YOLO("best.pt")


@st.cache_resource
def load_ocr():
    return easyocr.Reader(["en"])


model = load_model()
reader = load_ocr()

# -----------------------------
# VIDEO UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    # Save uploaded video temporarily
    temp_input = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )

    temp_input.write(uploaded_file.read())
    temp_input.close()

    input_path = temp_input.name

    st.success("✅ Video uploaded successfully!")

    # Show original video
    st.subheader("Original Video")
    st.video(input_path)

    # -----------------------------
    # PROCESS BUTTON
    # -----------------------------

    if st.button("🚀 Process Video"):

        output_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        ).name

        cap = cv2.VideoCapture(input_path)

        width = int(
            cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        height = int(
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        fps = cap.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 25

        total_frames = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )

        out = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (width, height)
        )

        progress_bar = st.progress(0)

        status = st.empty()

        frame_number = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            # -----------------------------
            # YOLO DETECTION
            # -----------------------------

            results = model(frame)

            for result in results:

                for box in result.boxes:

                    # Bounding box
                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    # Keep coordinates inside frame
                    x1 = max(0, x1)
                    y1 = max(0, y1)
                    x2 = min(width, x2)
                    y2 = min(height, y2)

                    # -----------------------------
                    # CROP NUMBER PLATE
                    # -----------------------------

                    plate = frame[
                        y1:y2,
                        x1:x2
                    ]

                    if plate.size == 0:
                        continue

                    # -----------------------------
                    # OCR
                    # -----------------------------

                    ocr_results = reader.readtext(
                        plate
                    )

                    detected_text = ""

                    for detection in ocr_results:

                        text = detection[1]

                        detected_text += text + " "

                    detected_text = detected_text.strip()

                    # -----------------------------
                    # DRAW BOUNDING BOX
                    # -----------------------------

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # -----------------------------
                    # DRAW OCR TEXT
                    # -----------------------------

                    if detected_text:

                        cv2.rectangle(
                            frame,
                            (x1, max(0, y1 - 40)),
                            (x2, y1),
                            (0, 255, 0),
                            -1
                        )

                        cv2.putText(
                            frame,
                            detected_text,
                            (x1 + 5, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 0),
                            2
                        )

            # Write processed frame
            out.write(frame)

            frame_number += 1

            # Progress
            if total_frames > 0:

                progress = (
                    frame_number / total_frames
                )

                progress_bar.progress(
                    min(progress, 1.0)
                )

                status.text(
                    f"Processing: "
                    f"{frame_number}/{total_frames} frames"
                )

        cap.release()
        out.release()

        progress_bar.progress(1.0)
        status.success("✅ Processing completed!")

        # -----------------------------
        # OUTPUT VIDEO
        # -----------------------------

        st.subheader("🎥 Processed Video")

        st.video(output_path)

        # -----------------------------
        # DOWNLOAD
        # -----------------------------

        with open(
            output_path,
            "rb"
        ) as video_file:

            st.download_button(
                label="⬇️ Download Processed Video",
                data=video_file,
                file_name="number_plate_ocr.mp4",
                mime="video/mp4"
            )

        st.success(
            "🎉 Number plate detection and OCR completed!"
        )
        