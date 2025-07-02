from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image

model = YOLO('best.pt')

def detect_image(pil_img):
    img = np.array(pil_img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = model(img)
    rendered = results[0].plot()
    rendered = cv2.cvtColor(rendered, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rendered)
