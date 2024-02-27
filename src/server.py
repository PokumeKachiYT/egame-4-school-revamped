from http.server import SimpleHTTPRequestHandler, HTTPServer
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        print("Error:", e)
        ip_address = None
    finally:
        s.close()

    return ip_address

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()
        print('hehe')

def init(port=8080):
    ip_address = get_ip_address()
    httpd = HTTPServer(('',port), MyRequestHandler)

    print(f"Server running on http://{ip_address}:{port}/")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    init()
