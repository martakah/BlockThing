import socket
import json
import requests
from threading import Thread
from socketserver import ThreadingMixIn
import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update( str(self.index).encode('utf-8') +
                    str(self.timestamp).encode('utf-8') + 
                    str(self.data).encode('utf-8')+ 
                    str(self.prev_hash).encode('utf-8'))
        return sha.hexdigest()


class ClientThread(Thread):
    
    def __init__(self, ip, port, prev_block, bchain):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.prev_block = prev_block
        self.bchain = bchain
        print("New server socket thread started for ", ip, ":", str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if data == 'exit':
                break
            else:
                print("Server received data: ",data.decode('ascii'))
                block_to_add = next_block(self.prev_block,data)
                self.bchain.append( block_to_add )
                self.prev_block = block_to_add
                print("Block",block_to_add.index," has been added!")
                print("Block contains the data- ",block_to_add.data)
                print("Hash is {}\n".format(block_to_add.hash))	
                print("The chain contains - ")
                for nodes in bchain:
                    print("Block is: ", nodes.index, " and Data is: ", nodes.data)
	

#            msg = input("Enter Response from Server/ Enter exit:")
#            if msg == 'exit':
#                break
#            conn.send(msg.encode('ascii'))


IP = '0.0.0.0'
PORT = 1234
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((IP, PORT))
threads = []




def origin_block():

    return Block(0, date.datetime.now(), "Origin Block", "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = data.decode('ascii')
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


bchain = [origin_block()]
prev_block = bchain[0]

while True:
	tcpServer.listen(4)
	print("Waiting for connection...")
	(conn, (ip,port)) = tcpServer.accept()
	newthread = ClientThread(ip,port,prev_block,bchain)
	newthread.start()
	threads.append(newthread)
	#	print('Got connection from',addr)
	#	msg = c.recv(1024)
	#	block_to_add = next_block(prev_block,msg)
	#	bchain.append( block_to_add )
	#	prev_block = block_to_add
	#	print("Block", block_to_add.index, " has been added!")
	#	print("Block contains the data - ", block_to_add.data)
	#	print("Hash is {}\n".format(block_to_add.hash))
	#	c.close()
for t in threads:
	t.join()
