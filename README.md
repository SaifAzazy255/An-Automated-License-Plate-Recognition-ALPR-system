# 🚗 Automated License Plate Recognition (ALPR) System

## 📌 Overview
This project implements an end-to-end Automated License Plate Recognition (ALPR) pipeline. It goes beyond simple object detection by utilizing robust tracking, dynamic pre-processing, and a virtual "Tripwire" logic to extract and log license plate text accurately from video streams.

## ✨ Key Features
*   **Custom Dataset Creation:** Raw video frames were extracted and manually annotated using **Roboflow** to ensure high-quality ground truth tailored to the specific environment.
*   **Stable Object Tracking:** Integrated **YOLOv8s** with ByteTrack to maintain consistent object IDs across frames and eliminate bounding box jitter.
*   **Enhanced OCR Pipeline:** Detected plates are dynamically cropped, upscaled (2x), and converted to grayscale to maximize the accuracy of **EasyOCR**.
*   **Resource Optimization (Tripwire Logic):** Engineered a virtual line mechanism using OpenCV. The OCR extraction and image saving processes are only triggered when a vehicle crosses a specific horizontal line, ensuring optimal capture angles and significantly reducing computational overhead.

## 🛠️ Tech Stack
*   **Deep Learning:** Ultralytics YOLOv8
*   **Computer Vision:** OpenCV
*   **OCR:** EasyOCR 
*   **Data Annotation:** Roboflow
*   **Language:** Python

