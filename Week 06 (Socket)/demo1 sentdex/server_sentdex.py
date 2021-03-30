import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(5)

while True:
    c, c_addr = s.accept()
    print(f'connection from {c_addr} has been established !!!')
    c.send(bytes('Welcome to the server', 'utf-8'))
    c.close()