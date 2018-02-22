import socket, threading
import struct, time
import hashlib, json, sys


class BC_Thread	(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		print("Starting "+ self.name)
		count = 2
		while(count >= 0):
			Functioning()
			count = count-1


		# Start running the thread which
		# will perform the following functions

		# 1. Validating transactions
		# 2. Creating blocks (adding transactions)		
		# 3. Add the block to the chain


# class Block:
# 	def __init__(self, index, data, prev_hash):	
#         contents = {'index':index, 'parentHash': prev_hash, 'txns': data}
#         self.hash = hash_block(contents)
#         self.block = {'Hash': self.hash, 'Contents': contents}
#         self.BlockStr = json.dumps(block, sort_keys=True)
#         #self.timestamp = timestamp #removed timestamp



def hash_block(msg=""):
	if type(msg)!=str:
		msg = json.dumps(msg,sort_keys=True)

	if sys.version_info.major == 2:
		return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
	else:
		return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

        #sha = hasher.sha256()
        # sha.update( str(self.index).encode('utf-8') +
        #             str(self.timestamp).encode('utf-8') + 
        #             str(self.data).encode('utf-8')+ 
        #             str(self.prev_hash).encode('utf-8'))
        #return sha.hexdigest()

def origin_block():
	initialTxn = {"FirstName": "10.0.0.1"}
	contents = {'index': 0, 'parentHash': "NONE", "txns": initialTxn}
	selfHash = hash_block(contents)
	selfBlock = {'Hash': selfHash, 'Contents': contents}
	selfBlockStr = json.dumps(selfBlock, sort_keys=True)
	return selfBlock


def next_block(txns, chain):
	parentBlock = chain[-1]
	parentHash  = parentBlock[u'Hash']
	blockNumber = parentBlock[u'Contents'][u'index'] + 1
	blockContents = {'index':blockNumber, 'parentHash':parentHash,'txns':txns}
	blockHash = hash_block( blockContents )
	block = {'Hash':blockHash,'Contents':blockContents}
	return block
    #txnCount    = len(txns)

    # this_index = last_block.index + 1
    # this_timestamp = date.datetime.now()
    # this_data = data.decode('ascii')
    # this_hash = last_block.hash
    # return Block(this_index, this_timestamp, this_data, this_hash)


def isValidTxn(txn, state):
		#This is where the digital signature logic will go
		return True



#This has to go in the thread
def Functioning():
	bchain = [origin_block()]

	dataList = {"Hey": "1st", "SSUP":"2nd", "ASB":"3rd"}
	blockSizeLimit = 5
	state = {}

	while len(dataList) > 0:
		bufferstart = len(dataList)

		txnList = []
		while (len(dataList) > 0 & len(txnList) < blockSizeLimit):
			newTxn = dataList.popitem()
			validity = isValidTxn(newTxn, state)
			if validity:           # If we got a valid state, not 'False'
				txnList.append(newTxn)
		        #state = updateState(newTxn,state)
			else:
			    print("ignored transaction")
			    sys.stdout.flush()
			    continue

		myBlock = next_block(txnList,bchain)
		bchain.append(myBlock)


	# for i in dataList:
	# 	block_to_add = next_block(self.prev_block, i)
	# 	bchain.append( block_to_add )
	# 	prev_block = block_to_add
	# 	print("Block",block_to_add.index," has been added!")
	#     print("Block contains the data- ",block_to_add.data)
	#     print("Hash is {}\n".format(block_to_add.hash))	
	    

	print("\nThe chain contains - ")
	for nodes in bchain:
	    print("Block hash is: ", nodes['Hash'], "\n and Contents are: ", nodes['Contents'])
