import socket
import os

HOST = 'localhost'
PORT = 9977

def handle_request(client_socket, request,client_address):
    request_lines = request.split('\r\n')
    print(f"Received request from {client_address}: {request_lines[0]}")
    method, path, _ = request_lines[0].split()

    if method == 'GET':
        if path == '/ar':
            path = '/main_ar.html'
        elif path == '/en':
            path = '/main_en.html'
        elif path == '/yt':
            response = 'HTTP/1.1 307 Temporary Redirect\r\nLocation: https://www.youtube.com\r\n\r\n'
            client_socket.sendall(response.encode())
            return
        elif path == '/so':
            response = 'HTTP/1.1 307 Temporary Redirect\r\nLocation: https://stackoverflow.com\r\n\r\n'
            client_socket.sendall(response.encode())
            return
        elif path == '/rt':
            response = 'HTTP/1.1 307 Temporary Redirect\r\nLocation: https://ritaj.birzeit.edu/register/\r\n\r\n'
            client_socket.sendall(response.encode())
            return

        file_extension = os.path.splitext(path)[1]

        if file_extension == '.html':
            content_type = 'text/html'
        elif file_extension == '.css':
            content_type = 'text/css'
        elif file_extension == '.png':
            content_type = 'image/png'
        elif file_extension == '.jpg':
            content_type = 'image/jpg'
        else:
            response = 'HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\r\n'
            response +='''
                <html>
                    <head>
                        <title>Error 404</title>
                        <style>
                            h1 { color: red; }
                                </style>
                    </head>
                </html>'''
            client_socket.sendall(response.encode())
            return

        with open('.' + path, 'rb') as file:
            content = file.read()
            response = f'HTTP/1.1 200 OK\r\nContent-type: {content_type}\r\n\r\n'.encode() + content
            client_socket.sendall(response)

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f'Server running at {HOST}:{PORT}...')

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode()

        handle_request(client_socket, request,client_address)

        client_socket.close()

if __name__ == "__main__":
    run()
