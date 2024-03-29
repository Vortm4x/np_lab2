from config import HOST, PORT
from socketserver import UDPServer, BaseRequestHandler
from responder import response

class UDPListener(BaseRequestHandler):
    def handle(self) -> None:

        request_data, socket = self.request

        response_data = response(request_data)
        socket.sendto(response_data, self.client_address)

if __name__ == '__main__':
    with UDPServer((HOST, PORT), UDPListener) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()