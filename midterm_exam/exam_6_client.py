from socket import *
import time

BUF_SIZE = 1024
LENGTH = 20

while True:
    #user_input = input()

    # 디바이스 1 소켓
    device1_socket = socket(AF_INET, SOCK_STREAM)
    device1_socket.connect(('localhost', 7777))

    #if user_input == '1':
    device1_socket.send(b'1')
    msg = device1_socket.recv(BUF_SIZE)
    temp = msg.decode()
    c = int.from_bytes(temp, 'big')
    string = f'Temp={c}, '
    print(string)

    #elif user_input == '2':
    device1_socket.send(b'2')
    msg = device1_socket.recv(BUF_SIZE)
    humid = msg.decode()
    string = f'Humid={humid}, '
    print(string)

    #elif user_input == '3':
    device1_socket.send(b'3')
    msg = device1_socket.recv(BUF_SIZE)
    lumi = msg.decode()
    string = f'Lumi={lumi}\n'
    print(string)

    #elif user_input == 'quit':
        #device1_socket.send(b'quit')
        #break