from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None) 
    while True: 
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            break
        else:
            if data.decode()=="ping":
                sock.sendto(b'ack', addr)
                print("Yes")
                msg = "pong"
                while True:
                    if random.random() <= 0.5:
                        continue
                    else:
                        sock.sendto(msg.encode(), addr)
                    try:
                        data, addr = sock.recvfrom(BUFF_SIZE)
                    except timeout:
                        continue
                    else:
                        break
            else:
                break

    
        
        
        