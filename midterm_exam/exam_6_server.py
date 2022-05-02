from socket import *
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

while True:
    con, addr = sock.accept()
    msg = con.recv(BUF_SIZE)
    if not msg:
        con.send(f'{0}'.encode())
        con.close()
        continue
    elif msg == b'quit':
        #print('client: ', addr, msg.decode())
        con.close()
        continue
    elif msg == b'1':
        #print('client: ', addr, msg.decode())
        temp = random.randint(0, 40)
        a = temp.to_bytes(4, 'big')
        con.send(a)
        continue
    elif msg == b'2':
        humid = random.randint(0, 100)
        con.send(f'{humid}'.encode())
        continue
    elif msg == b'3':
        illum = random.randint(70, 150)
        con.send(f'{illum}'.encode())
        break

    # conn.close()