from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('계산식을 입력하세요 : ')
    if msg == 'q':
        break

    s.send(msg.encode())

    print('결과:', s.recv(1024).decode())
s.close()