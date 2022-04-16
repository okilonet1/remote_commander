import time
import socket
import os
import sys

s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind(('', port))
s.listen()
conn, addr = s.accept()
print(addr, "is connected")
command = input(str("Enter command: "))
conn.send(command.encode())
print("Command sent")
data = conn.recv(1024)
if data:
    print("command received and executing")
