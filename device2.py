from socket import *
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)

while True:
    con, addr = sock.accept()
    msg = con.recv(BUF_SIZE)
    if not msg:
        con.close()
        continue
    elif msg == b'quit':
        print('client: ', addr, msg.decode())
        con.close()
        continue
    elif msg == b'Request':
        print('client: ', addr, msg.decode())

        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        con.send(f'{heartbeat}/{steps}/{cal}'.encode())

    # conn.close()