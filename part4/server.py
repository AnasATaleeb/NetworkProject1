import socket
import time

class Server:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((server_ip, server_port))
        self.clients = {}  # Dictionary to store client information

    def run(self):
        print("Server is running. Waiting for messages...")

        while True:
            data, client_address = self.server_socket.recvfrom(1024)

            # Extract client information from the message
            message_parts = data.decode().split(',')
            client_name = message_parts[0]
            message = message_parts[1]

            # Update client's last message time
            self.clients[client_address] = (client_name, message, time.time())

            print(f"Received message from {client_name} at {client_address}")

            # Print the list of last received messages
            print("Last received messages:")
            for index, (address, (name, message, timestamp)) in enumerate(self.clients.items(), start=1):
                print(f"{index}- Received message from {name} at {address} at {time.ctime(timestamp)}")

            print("")  # Empty line for separation


if __name__ == "__main__":
    server = Server("", 8855)  # Replace with your server IP and port
    server.run()
