import socket
import time

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8001))
    server_socket.listen(5)

    print("Subprocess 2 running...")

    while True:
        # Accept incoming connections
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")

        # Send messages
        while True:
            client_socket.sendall(b"Hello from subprocess 2!\n")
            time.sleep(3)  # Sleep for 3 seconds

if __name__ == "__main__":
    main()
