import socket
import numpy

sock = socket.socket()
sock.connect(('localhost', 9092))
sock.recv(1024).decode("cp866")
while True:
    data=sock.recv(1024).decode("cp866")
    print(data)
    text=data[1:-2].split(", ")
    a=[int(text[i]) for i in range (100)]
    print(a)
    sock.send (str(numpy.sum(a)).encode())
