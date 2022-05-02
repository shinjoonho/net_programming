import socket
import random
import threading
import time
sock = socket.socket()
sock.connect(('localhost',9000))

data = sock.recv(1024)

def send(sock):
    while True:

        heart = random.randint(40,140)
        steps = random.randint(2000,6000)
        cal = random.randint(1000,4000)


        msg =  'Device 2 : Heartbeat={}, Steps={}, Cal={}'.format(heart,steps,cal)
        sock.send(msg.encode())
        time.sleep(5)

if 'Receive' in data.decode():
    th = threading.Thread(target=send,args=(sock,))
    th.start()