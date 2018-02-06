import socket
import sys
from _thread import *

host = ''
port = 8888

if len(sys.argv) == 1:
    print('No port number specified. Using default 8888')
elif len(sys.argv) == 2:
    if len(sys.argv[1]) == 4:
        port = int(sys.argv[1])
    else:
        print("Port length must be exactly four digits.")
        sys.exit()
else:
    print("Invalid number of arguments: server.py expects 1 or 2.")
    print('Arguments: ' + str(len(sys.argv)))
    sys.exit()    


#Check Arguments
print('Arguments: ' + str(len(sys.argv)))
print('Port:' + str(port))

#Open Socket Type
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("Failed to Connect")
    sys.exit();
    
print("Socket Created with port number " + str(port))

try:
    s.bind((host,port))
except socket.error:
    print("Binding Failed")
    sys.exit()
    
print("Socket Bounded")

#Listening

s.listen(10) #10 in listen queue

print("Socket Ready")

#client thread function
def clientThread(conn, socket):
    welcomeMessage = "Type something: \n"
    conn.send(welcomeMessage.encode())
    
    while 1:
        data = conn.recv(1024)
        reply = "MESSAGE:" + data.decode()
        if not data:
            break
        print(reply)
        conn.sendall(data)
    
    conn.close()


#Allow continuous stream
while 1:
    conn, addr = s.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientThread, (conn, addr[1]))
    
#Close on Receive
conn.close()
s.close()

