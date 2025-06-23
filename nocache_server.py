import http.server
import socketserver
import time

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_response_only(self, code, message=None):
        super().send_response_only(code, message)
        self.send_header('Last-Modified', self.date_time_string(time.time()))
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

handler = NoCacheHTTPRequestHandler
with socketserver.TCPServer(("", 8000), handler) as httpd:
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
