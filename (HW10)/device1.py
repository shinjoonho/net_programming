import socket
import random
import threading
import time

sock = socket.socket()
sock.connect(('localhost',9000))
data = sock.recv(1024)
if not data:
    sock.close()

def send(sock):
    while True:
        temp = random.randint(0,40)
        humid = random.randint(0,100)
        lilum = random.randint(70,150)

        msg =  'Device 1 : Temp={}, Humid={}, lilum={}'.format(temp,humid,lilum)
        sock.send(msg.encode())
        time.sleep(3)
th = threading.Thread(target=send,args=(sock,))

if 'Receive' in data.decode():
    print('received')
    th.start()