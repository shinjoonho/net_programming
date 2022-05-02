import socket
import selectors
import time

sel = selectors.DefaultSelector()

def accept(conn,mask):
    cli, addr = conn.accept()
    print('connect from',addr)
    cli.send(b'Receive')
    sel.register(cli,selectors.EVENT_READ,save)

def save(cli,mask):
    print('function call')
    data = cli.recv(1024)
    if not data:
        cli.close()

    current_time = time.strftime('%c', time.localtime(time.time()))
    msg = current_time + ":" + data.decode() +'\n'

    file = open('data.txt','a')
    file.write(msg)
    file.close()

sock = socket.socket()
sock.bind(('',9000))
sock.listen(2)

sel.register(sock,selectors.EVENT_READ,accept)
while True:    
    evnets = sel.select()
    for key,mask in evnets:
        callback = key.data
        callback(key.fileobj,mask)