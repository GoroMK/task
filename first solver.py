import socket

sock = socket.socket()
sock.connect(('localhost', 9092))
sock.recv(1024).decode("cp866")
while True:
    text=sock.recv(1024).decode("cp866")
    print(text)
    a,b=text.split(" ")[0],text.split(" ")[1]
    sock.send (str(int(a)*int(b)).encode())
