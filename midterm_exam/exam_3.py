import socket

ip = '220.69.189.125'
port = 443

print(socket.getfqdn(ip))
print(socket.getservbyport(port))
url = '{}://{}'.format(socket.getservbyport(port),socket.getfqdn(ip))
print(url)
print(socket.inet_aton(ip))