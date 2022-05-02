

from http import client
from lib2to3.pgen2.token import OP
from pydoc import cli
import re
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',3333))
s.listen(5)

print("waiting..")

operator = ["+","-","*","/"]
while True:
    client, addr = s.accept()
    print("connect from ", addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        
        #입력 값 고려 공백 초기화
        data = data.decode().replace(" ","")
        print("input",data)

        # split 사용 위한 공백 생성
        for x in data:
            if(x in operator):
                a, b = data.split(x)

                a = int(a)
                b = int(b)

                if x == '+':
                    result = a+b
                elif x == '-':
                    result = a-b
                elif x == '*':
                    result = a*b
                elif x == '/':
                    result = round(float(a/b),1)

        client.send(str(result).encode())
        
    client.close()   