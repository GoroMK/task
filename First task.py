import socket
import random
import time



count=0

sock = socket.socket()
sock.bind(('localhost', 9092))
sock.listen(5)
conn, addr = sock.accept()
print ('connected:', addr)
conn.send("Данны два числа.\nПермножте их\n".encode("cp866"))
while count<100:
    a,b=random.randint(100,999),random.randint(100,999)
    conn.send((str(a)+" "+str(b)+'\n').encode())
    time1=time.time()
    text=conn.recv(1024).decode()
    if int(text) !=a*b:
        exit()
    time2=time.time()
    if time2>time1+5:
        exit()
    count+=1
conn.send ("CTFUS_{Ch0t_1z1_ta5k_nad0_s0jn33}".encode())


