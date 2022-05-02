from socket import *
import random

s = socket()
s.bind(('', 9000))
s.listen(10)

while True:
    con, addr = s.accept()
    msg = con.recv(1024).decode()
    if msg == "Request":
        print('client: ', addr, msg)
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        con.send(f'{temp}/{humid}/{illum}'.encode())
    
    elif msg == "quit":
        con.close()
        break
