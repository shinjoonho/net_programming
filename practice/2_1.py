import socket

sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send(b'Shin Joonho')# 본인의 이름을 문자열로 전송
qw = sock.recv(1024)# 본인의 학번을 수신 후 출력
er=int.from_bytes(qw, 'big')
print(er)
sock.close()