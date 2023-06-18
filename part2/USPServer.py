import socket
from datetime import datetime

UDP_IP = "192.168.85.63"  # Listen on all available network interfaces
UDP_PORT = 8855

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))
client_count = 0
client_messages = {}

# Create an empty hashmap
hashmap = {}

while client_count < 3:
    print("==============================================================")
    print("Server: Anas Taleeb")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Receive data from a client
    data, addr = sock.recvfrom(1024)

    message = data.decode()

    # Add the client's message to the dictionary
    if addr[0] not in client_messages:
        client_messages[addr[0]] = message
        client_count += 1

    # Add key-value pairs to the hashmap
    hashmap[message] = timestamp
    i = 1
    # Traverse the dictionary using a for loop
    for key in hashmap.keys():
        value = hashmap[key]
        # Print the last received message from each client
        print(i, " ) Received Message from ", ":", key, " At :", value)
        i = i + 1

# Close the socket
sock.close()
