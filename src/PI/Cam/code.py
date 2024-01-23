from flask import Flask, render_template, Response
from threading import Thread
import cv2
import time
import serial

app = Flask(__name__)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height
cap.set(5, 120)  # Set frame rate

# Initialize UART (replace '/dev/ttyUSB0' with your actual UART device)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
message_list = []

# Function to capture frames in a separate thread
def capture_frames():
    global message_list
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        current_frame = (b'--frame\r\n'
                         b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
        yield current_frame
        time.sleep(0.033)  # 33 milliseconds delay for approximately 30Hz

# Function to fetch UART data in a separate thread
def fetch_uart_data():
    global message_list
    while True:
        message_list.append(ser.readline().decode('utf-8').strip())
        if len(message_list) > 10:
            message_list.pop(0)
        time.sleep(0.1)  # Adjust the sleep time based on UART data rate

# Routes remain unchanged
@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/api/uart-data')
def get_uart_data():
    global message_list
    uart_data = "\n".join(message_list)
    return uart_data

@app.route('/video_feed')
def video_feed():
    return Response(capture_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Start the threads
if __name__ == '__main__':
    capture_thread = Thread(target=capture_frames)
    uart_thread = Thread(target=fetch_uart_data)

    capture_thread.start()
    uart_thread.start()

    app.run(host='0.0.0.0', port=5000, debug=False)
