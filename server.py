import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    for port in [3000, 8080, 5000, 8000]:
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"Radha-Krishna 3D Story Server running at http://localhost:{port}/")
                sys.stdout.flush()
                httpd.serve_forever()
        except OSError:
            continue

if __name__ == "__main__":
    run_server()
