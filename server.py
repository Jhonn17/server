import socket

server = socket.socket()

server.bind(("192.168.1.133", 8000))

server.send()