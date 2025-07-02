from flask import Flask, render_template, request, send_file
from PIL import Image
import base64, io
from yolov11_model import detect_image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    image_data = base64.b64decode(data['image'].split(',')[1])
    image = Image.open(io.BytesIO(image_data)).convert('RGB')

    output_image = detect_image(image)
    buf = io.BytesIO()
    output_image.save(buf, format='JPEG')
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
