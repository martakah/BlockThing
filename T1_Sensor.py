import socket
import struct
import sys
import threading
import time

class SensorThread(threading.Thread):

	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		print("Starting "+ self.name)
		sensor_thread(self)



def sensor_thread(threadname):
	print(threadname.name + " with the id " + threadname.threadID + " started.\n")
	multicast_group = '224.3.29.71'
	server_address = (multicast_group, 10000)
	#print(server_address)

	# Create the socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#This will enable the reuse of the local address so that multiple
	#applications can use at the same time that multicast port

	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Bind to the server address
	sock.bind(server_address)
	sock.settimeout(8) #Set this to make Thread 1 exit after 5 seconds of inactivity

	# Tell the operating system to add the socket to the multicast group
	# on all interfaces.
	group = socket.inet_aton(multicast_group)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

	# Receive/respond loop
	while True:
		try:
			print ('\nwaiting to receive message', file=sys.stderr)
			data, address = sock.recvfrom(1024)

			print('received ', len(data), 'bytes from ',address, file=sys.stderr)
			print(data.decode('utf-8'), file=sys.stderr)
			print ( 'sending acknowledgement to', address, file = sys.stderr)
			ack = 'ack by s1'
			sock.sendto(ack.encode('utf-8'), address)
		except:
			print("Interrupt Occurred")
			break