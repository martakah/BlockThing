import socket 

host = socket.gethostname() 
port = 1234
BUFFER_SIZE = 2000 
msg = input("tcpClientB: Enter message/ Enter exit:") 
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while msg != 'exit':
    tcpClientB.send(msg.encode('ascii'))
#    data = tcpClientB.recv(BUFFER_SIZE)
#    print(" Client received data:", data.decode('ascii'))
    msg = input("tcpClientB: Enter message to continue/Enter exit:")
    
tcpClientB.close() 
