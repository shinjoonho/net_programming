from socket import *
from collections import deque

BUFF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET,SOCK_DGRAM)
s_sock.bind(('',port))

mboxID = {}

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    req = data.decode()
    
    if req.startswith('send'):
        tmp = list(req.split())
        id = tmp[1]
        msg = tmp[2:]
        mesg = ''

        for i in tmp[2:]:
            mesg = str(mesg) + i + ' '
        print (mesg)

        if id not in mboxID:
            mboxID[str(id)] = deque()
            mboxID[str(id)].append(mesg)
            print("mesg came")

        else:
            mboxID[str(id)].append(mesg)

    elif req.startswith('receive'):
        req_box = req.split()[1]

        if req_box in mboxID:
            if mboxID[str(req_box)]:
                sndMsg = mboxID[str(req_box)].popleft()
                s_sock.sendto(sndMsg.encode(),addr)
            else:
                s_sock.sendto("no messages".encode(),addr)
        
        else:
            s_sock.sendto("no messages".encode(),addr)

    elif req.startswith('quit'):
        s_sock.close()