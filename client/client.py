from tkinter import *
from tkinter import ttk
import socket


print("""

Welcome to the PloopyChat Client!

Please Enter your name and ChatID

""")

userChoice = input("Name: ")
ChatID = input("ChatID: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345


s.connect(("127.0.0.1",12345))
message = s.recv(2048).decode
print(message)

while True:
    s.send(input("").encode())


