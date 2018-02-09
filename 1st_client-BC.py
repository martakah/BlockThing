import socket 

host = socket.gethostname() 
port = 1234
BUFFER_SIZE = 2000 
msg = input("tcpClientA: Enter message/ Enter exit:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while msg != 'exit':
    tcpClientA.send(msg.encode('ascii'))
#    data = tcpClientA.recv(BUFFER_SIZE)
#    print(" Client2 received data:", data.decode('ascii'))
    msg = input("tcpClientA: Enter message to continue/Enter exit:")

    if msg == 'exit':
        tcpClientA.send(msg.encode('ascii'))
        
tcpClientA.close()
