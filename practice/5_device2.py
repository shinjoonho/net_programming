from socket import *
import random

s = socket()
s.bind(('', 8000))
s.listen(10)

while True:
    con, addr = s.accept()
    msg = con.recv(1024).decode()
    if msg == "Request":
        print('client: ', addr, msg)
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        con.send(f'{heartbeat}/{steps}/{cal}'.encode())
    
    elif msg == "quit":
        con.close()
        break