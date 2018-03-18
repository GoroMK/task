import socket
import random
import time

count=0
articls="CTFUS is the best CTF in the world and this task confirm it"

sock = socket.socket()
sock.bind(('localhost', 9092))
sock.listen(5)
conn, addr = sock.accept()
print ('connected:', addr)
conn.send("Данн текст.\nОпределите сколько данных букв в данном тексте в разных регистрах\n".encode("cp866"))
conn.send((articls+"\n").encode())
while count<50:
    number=0
    litter=chr(random.randint(97,122))
    conn.send(("Сколько букв "+litter+"\n").encode("cp866"))
    time1=time.time()
    litteru=litter.upper()
    for word in articls:
        if word==litteru or word==litter:
            number+=1
    print(number)
    text=conn.recv(1024).decode()
    if int(text) !=number:
        exit()
    time2=time.time()
    if time2>time1+5:
        exit()
    count+=1
conn.send ("CTFUS_{0tl1chn11_ta5k_p0cht1_1dealn11}".encode())
