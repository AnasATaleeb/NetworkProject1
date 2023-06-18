import socket
import threading
import time

UDP_IP = "192.168.85.63"  # Broadcast IP Server address
UDP_PORT = 8855
MESSAGE = "Raghad AbuRemeleh"  # Replace with the student's name

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    try:
        # Send a broadcast message to the server
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        # print("Sent broadcast message:", MESSAGE)
        print("Sent broadcast message:", MESSAGE)
    except OSError as e:
        print("Error sending message:", str(e))

    # Wait for 2 seconds before sending the next message
    time.sleep(2)

# Close the socket (Note: This code is never reached in this infinite loop)
sock.close()
