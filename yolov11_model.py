from ultralytics import YOLO
import cv2

# Load your model
model = YOLO("best.pt")

def detect_frame(frame):
    results = model(frame)
    annotated = results[0].plot()
    return annotated
