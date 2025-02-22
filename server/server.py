import os
import socket
import subprocess
from asyncio import sleep

s = socket.socket()

port=12345
s.bind(('', port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listening")

c, addr = s.accept()
print ('Got conn from', addr)
c.send("Welcome to the server!".encode())
while True:
    cmd = c.recv(1024).decode()
    print(cmd)