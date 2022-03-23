import socket
sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

str = 'Joonho Shin'
sock.send(str.encode())

b = sock.recv(4)
c = int.from_bytes(b, 'big')
print(c)

sock.close()