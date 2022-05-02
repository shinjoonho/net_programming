from socket import *
import random
import time

PORT = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', PORT)
while True:
    msg = "ping"
    reTx = 0
    while reTx <= 2:  
        sock.sendto(msg.encode(), addr)
        start = time.time()
        #print(start)
        sock.settimeout(1)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 2:
        print("Fail")
        break

    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    if data.decode() == "pong":
        end = time.time()
        #print(end)
        RTT = end - start
        #print(RTT)
        print("Success (RTT: {})".format(RTT))
        break
    else:
        print("Fail")
        break