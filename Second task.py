import socket
import random
import time
import numpy



count=0

sock = socket.socket()
sock.bind(('localhost', 9092))
sock.listen(5)
conn, addr = sock.accept()
print ('connected:', addr)
conn.send("Данн массив.\nНайдите сумму эллементов\n".encode("cp866"))
while count<100:
    a=[random.randint(0,100) for i in range(100)]
    conn.send((str(a)+"\n").encode())
    time1=time.time()
    text=conn.recv(1024).decode()
    if int(text) !=numpy.sum(a):
        exit()
    time2=time.time()
    if time2>time1+10:
        exit()
    count+=1
conn.send ("CTFUS_{Nu_p0cht1_n0_v5e_eshe_ne_t0}".encode())
