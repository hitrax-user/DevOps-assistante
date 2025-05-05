from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

class HealthCheckHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            super().do_GET()

with HTTPServer(('0.0.0.0', PORT), HealthCheckHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
