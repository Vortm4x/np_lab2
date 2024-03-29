from config import HOST, PORT
from socketserver import BaseRequestHandler, TCPServer
from responder import response

class TCPListener(BaseRequestHandler):
    def handle(self) -> None:
        socket = self.request
        request_data = socket.recv(1024).strip()

        response_data = response(request_data)
        socket.sendall(response_data)

if __name__ == '__main__':
    with TCPServer((HOST, PORT), TCPListener) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()