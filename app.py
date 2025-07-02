from flask import Flask, render_template, Response
import cv2
from yolov11_model import detect_frame

app = Flask(__name__)
cap = cv2.VideoCapture(0)  # Webcam

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            detected = detect_frame(frame)
            _, buffer = cv2.imencode('.jpg', detected)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
