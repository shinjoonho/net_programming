from socket import *

#table = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',\
#            '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            a, op, b = data.decode().split()
            if op == '+':
                result = int(a) + int(b)
            elif op == '-':
                result = int(a) - int(b)
            elif op == '*':
                result = int(a) * int(b)
            else:
                result = round(float(a) / float(b), 1)
        except:
            client.send(b'Try again')
        else:
            client.send(str(result).encode())
    client.close()