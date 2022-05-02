import socket
a = 12345678
b = str(a)
print(b)

c = b.encode()
print(c)

d = c.decode()
print(d)
print(type(d))
e = int(d)
print(e)
print(type(e))


a = 1
b = a.to_bytes(4,'big')
print(b)

c = int.from_bytes(b,'big')
print(c)