# Reverse-Shell
A basic reverse-shell python script , which uses the sockets module.


# How it works
- The attacker runs the attacker.py script , the victim is socially engineered in such a way that they run the victim.py script
- When the attacker runs the attacker.py script , it will create a TCP socket , and will listen out for incoming connection attempts
- When the client runs the victim.py script , the script will repeatedly try to connect to the attcker's IP address over the port specified by the attacker
- When a connection is established , the victim.py script will find the directory that it is being ran from, and will send that to the attacker.
- After this , the attacker can input basic commands , which are sent over the socket to the victim script , which then runs these commands using the subprocess module.
- The victim script will then take the output of the command , and send it back over to the attacker script , where it is displayed
- The attacker enters the letter "q" when they are finished.

# Troubleshooting

NOTE THAT THIS SCRIPT IS NOT PARTICULARLY EFFECTIVE IN REAL WORLD SCENARIOS - IT IS MORE OF A PROOF OF CONCEPT

DO NOT run commands that take further input , as the scripts are not programmed to handle this and will freeze - I may look in to changing this in future.
If the script freezes , you will have to reset the connection - this requires both the victim and attacking script be run again. I may look in to amending this such that only the attcking script needs to be run again.

If receiving "ADDRESS ALREADY BEING USED - WAIT A MINUTE AND TRY AGAIN" , then:
 - Try running the script from a new terminal
 - If you don't want to wait for the socket to time out , then go to the code and change the port you are connecting over - THIS MUST BE DONE FOR BOTH SCRIPTS
 - If that doesnt work , then wait for a few miniutes and run the script again
 - If that does not work then try killing the process
 - Finally , if that doesn't work then turn your computer on and off again

If receving
