import socket
import struct
import sys

message = "very important data"
multicast_group = ('224.3.29.71', 10000)

#create datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set a timeout for the client to receive the response
sock.settimeout(100)

#Setting the TTL for msgs to 1 so that they do not go beyond the local network
ttl = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
	# Send data to the multicast group
	print( 'sending "', message, '"', file= sys.stderr)
	val = message.encode('utf-8')
	sent = sock.sendto(val, multicast_group)

    # Look for responses from all recipients
	while True:
		print('waiting to receive', file = sys.stderr)
		try:
		    data, server = sock.recvfrom(16)
		except socket.timeout:
		    print ('timed out, no more responses', file = sys.stderr)
		    break
		else:
		    print('received ', data.decode('utf-8'), 'from ',server, file=sys.stderr)

finally:
	print('closing socket', file = sys.stderr)
	sock.close()

