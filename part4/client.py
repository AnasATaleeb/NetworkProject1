import socket
import time

class Client:
    def __init__(self, client_ip, server_ip, server_port, client_name):
        self.client_ip = client_ip
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.client_name = client_name

    def send_message(self, message):
        full_message = f"{self.client_name},{message}".encode()
        self.client_socket.sendto(full_message, (self.server_ip, self.server_port))
        print(f"Sent message from {self.client_name} to {self.server_ip}:{self.server_port}")

    def run(self):
        while True:
            message = input("Enter your message: ")
            self.send_message(message)
            time.sleep(2)


if __name__ == "__main__":
    client = Client("192.168.1.241", "192.168.1.255", 8855, "Anas Taleeb")  # Replace with your IPs, port, and name
    client.run()
