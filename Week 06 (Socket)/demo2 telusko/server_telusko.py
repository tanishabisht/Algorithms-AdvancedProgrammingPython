import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created!')

# RANGE FOR PORT NUMBER: 0 - 65535
s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connections')

while True:
    c, c_addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with ', c_addr, name)    
    c.send(bytes('Welcome to Telusko', 'utf-8'))
    c.close()