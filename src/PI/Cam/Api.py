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
from http.server import SimpleHTTPRequestHandler, HTTPServer
import serial

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