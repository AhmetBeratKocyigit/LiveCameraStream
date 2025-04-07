from flask import Flask, Response
import cv2 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Kamera bağlantısı
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera açılamadı.")    


def generate():  
    while True:
        ret, frame = cap.read()  # Kameradan bir kare al
        if not ret:
            break
        
        # JPEG formatında kareyi encode et
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        
        # JPEG'i stream olarak gönder
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
