import socket
import requester
from config import HOST, PORT


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        request_data = requester.prepare()
        client_socket.sendall(request_data)
        
        response_data = client_socket.recv(1024).decode()
        requester.handle(response_data)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error occurred: {e}")
