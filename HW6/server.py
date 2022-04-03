from socket import *
from collections import deque
import random

BUFF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
box = {}

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    request = data.decode()

    if request.startswith('send'):
        temp = list(request.split())
        box_id, message = temp[1], temp[2:]
        message = " ".join(message)
        if box_id not in box:
            box[str(box_id)] = deque([message])
            print(f"LOG : [{box_id}] <- '{message}'")
        else:
            box[str(box_id)].append(message)
            print(f"LOG : [{box_id}] <- '{message}'")

    elif request.startswith('receive'):
        box_id = request.split()[1]
        if box_id not in box:
            print(f"LOG : [{box_id}] box doesn't exist -> send failed")
            s_sock.sendto("No messages".encode(), addr)
        else:
            if box[str(box_id)]:
                print(f'LOG : [{box_id}] box has message -> send to [{addr}]')
                s_sock.sendto(box[str(box_id)].popleft().encode(), addr)
            else:
                print(f'LOG : [{box_id}] box has not message -> send failed')
                s_sock.sendto("No messages".encode(), addr)