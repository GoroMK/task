import socket


sock = socket.socket()
sock.connect(('localhost', 9092))
sock.recv(1024)
articl=sock.recv(1024).decode("cp866")
print(articl)
while True:
    number=0
    data=sock.recv(1024).decode("cp866")
    print(data)
    for letter in articl:
        if letter==data[-2] or letter==data[-2].upper():
            number+=1
    print(number)
    sock.send(str(number).encode())

