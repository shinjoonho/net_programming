from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))


while True:
    msg = input('Enter the message("send [mBoxID] message" or "receive [mBoxID]) : ')
    if msg.startswith('send'):  
        c_sock.sendto(msg.encode(), ('localhost', port))
        print('OK')
    elif msg.startswith('receive'):  
        c_sock.sendto(msg.encode(), ('localhost', port))
        data, addr = c_sock.recvfrom(BUFF_SIZE)
        print(data.decode())
    elif msg == 'quit':
        c_sock.sendto('quit'.encode(), ('localhost', port))
        break
    else:
        print('Invalid Input')


c_sock.close()