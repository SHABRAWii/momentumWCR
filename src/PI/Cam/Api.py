# from http.server import SimpleHTTPRequestHandler, HTTPServer
# import serial

# ser = serial.Serial('/dev/ttyUSB0', 9600)
# message_list = []
# class UARTRequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/api/uart-data':
#             # Replace this with actual UART data
#             global message_list
#             message_list.append(ser.readline().decode('utf-8').strip())
#             if len(message_list) > 10:
#                 message_list.pop(0)
#             uart_data = "\n".join(message_list)
            
#             self.send_response(200)
#             self.send_header('Content-type', 'text/plain')
#             self.end_headers()
#             self.wfile.write(uart_data.encode('utf-8'))
#         else:
#             super().do_GET()

# server_address = ('', 8000)
# httpd = HTTPServer(server_address, UARTRequestHandler)
# print('Server started on port 8000...')
# httpd.serve_forever()
# from http.server import SimpleHTTPRequestHandler, HTTPServer
# import serial

# ser = serial.Serial('/dev/ttyUSB0', 9600)
# message_list = []

# class CombinedRequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             # Serve the combined HTML file
#             with open('combined_page.html', 'rb') as file:
#                 self.send_response(200)
#                 self.send_header('Content-type', 'text/html')
#                 self.end_headers()
#                 self.wfile.write(file.read())
#         elif self.path == '/api/uart-data':
#             # Replace this with actual UART data
#             global message_list
#             message_list.append(ser.readline().decode('utf-8').strip())
#             if len(message_list) > 10:
#                 message_list.pop(0)
#             uart_data = "\n".join(message_list)
            
#             self.send_response(200)
#             self.send_header('Content-type', 'text/plain')
#             self.end_headers()
#             self.wfile.write(uart_data.encode('utf-8'))
#         else:
#             super().do_GET()

# # Use a try-except block to gracefully handle server shutdown
# try:
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, CombinedRequestHandler)
#     print('Server started on port 8000...')
#     httpd.serve_forever()
# except KeyboardInterrupt:
#     print('Server shutting down...')
#     httpd.server_close()
from http.server import SimpleHTTPRequestHandler, HTTPServer
import serial
import cv2
from time import sleep
vid = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyUSB0', 9600)
message_list = []

class CombinedRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the combined HTML file
            with open('combined_page.html', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/api/uart-data':
            # Replace this with actual UART data
            global message_list
            message_list.append(ser.readline().decode('utf-8').strip())
            if len(message_list) > 10:
                message_list.pop(0)
            uart_data = "\n".join(message_list)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(uart_data.encode('utf-8'))
        elif self.path == '/api/camera-feed':
            # Capture an image from the camera and serve it
            try:
                # Create a VideoCapture object
                cap = cv2.VideoCapture(0)

                # Wait for the camera to warm up
                sleep(2)

                # Capture a single frame
                ret, frame = cap.read()

                # Release the camera capture object
                cap.release()

                # Convert the frame to JPEG format
                _, image_data = cv2.imencode('.jpg', frame)
                
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.send_header('Content-length', len(image_data))
                self.end_headers()
                self.wfile.write(image_data.tobytes())
            except Exception as e:
                print(f"Error capturing image: {e}")
                self.send_error(500, "Internal Server Error")
        else:
            super().do_GET()

# Use a try-except block to gracefully handle server shutdown
try:
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CombinedRequestHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Server shutting down...')
    httpd.server_close()
