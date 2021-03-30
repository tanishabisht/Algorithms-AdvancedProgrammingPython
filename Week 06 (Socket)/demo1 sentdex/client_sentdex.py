import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

while True:
    msg = s.recv(1024)
    print(msg.decode('utf-8'))

# while True:
#     msg = s.recv(8)
#     print(msg.decode('utf-8')) 