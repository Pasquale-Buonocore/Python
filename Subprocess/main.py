import socket
import subprocess

def main():
    # Start subprocesses
    subprocess.Popen(["python", "subprocess1.py"])
    subprocess.Popen(["python", "subprocess2.py"])

    # Create client sockets
    client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket1.connect(('localhost', 8000))

    client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket2.connect(('localhost', 8001))

    while True:
        # Check for messages on subprocess 1 socket
        try:
            data = client_socket1.recv(1024)
            if data:
                print(data.decode())
        except ConnectionResetError:
            print("Connection with subprocess 1 reset.")
            break

        # Check for messages on subprocess 2 socket
        try:
            data = client_socket2.recv(1024)
            if data:
                print(data.decode())
        except ConnectionResetError:
            print("Connection with subprocess 2 reset.")
            break

    # Close sockets
    client_socket1.close()
    client_socket2.close()

if __name__ == "__main__":
    main()
