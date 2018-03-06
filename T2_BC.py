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
		Functioning()
		


def hash_block(msg=""):
	if type(msg)!=str:
		msg = json.dumps(msg,sort_keys=True)

	if sys.version_info.major == 2:
		return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
	else:
		return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

        
def origin_block():
	initialTxn = {"FirstName": 0}
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
    

def isValidTxn(txn, state):
		#This is where the digital signature logic will go
		return True


def updateState(txn, state):
	state = state.copy() # As dictionaries are mutable, avoid confusion
	for key in txn:
		if key in state.keys():
			state[key] += txn[key]
		else:
			state[key] = txn[key]
	return state



def checkHash(block):
	#checks the block hash; raises exception if hash does not match
	#the contents of the block.
	expected = hash_block( block['Contents'] )
	if block['Hash'] != expected:
		raise Exception('Hash does not match the block contents')
	return



def checkBlockValidity(block,parent,state):    
    
    parentNumber = parent['Contents']['index']
    parentHash   = parent['Hash']
    index  = block['Contents']['index']
    
    
    for txn in block['Contents']['txns']:
        if isValidTxn(txn,state):
            state = updateState(txn,state)
        else:
            raise Exception('Invalid transaction in block %s: %s'%(index,txn))

    checkHash(block)

    if index!=(parentNumber+1):
        raise Exception('Hash does not match contents of block %s'%index)

    if block['Contents']['parentHash'] != parentHash:
        raise Exception('Parent hash not accurate at block %s'%index)
    
    return state



def checkChain(chain):
    
    if type(chain)==str:
        try:
            chain = json.loads(chain)
            assert( type(chain)==list)
        except:  
            return False
    elif type(chain)!=list:
        return False
    
    state = {}

    for txn in chain[0]['Contents']['txns']:
        state = updateState(txn,state)
    checkHash(chain[0])
    parent = chain[0]
    
    for block in chain[1:]:
        state = checkBlockValidity(block,parent,state)
        parent = block
        
    return state



#This has to go in the thread
def Functioning():
	bchain = [origin_block()]

	dataList = [{"Hey": 1}, {"SSUP": 2}, {"ASB":3}]
	blockSizeLimit = 5
	state = {u'FirstName':0}

	while len(dataList) > 0:
		bufferstart = len(dataList)

		txnList = []
		while (len(dataList) > 0 & len(txnList) < blockSizeLimit):
			newTxn = dataList.pop()
			validity = isValidTxn(newTxn, state)
			if validity:
				# If we got a valid state, not 'False'
				txnList.append(newTxn)
				state = updateState(newTxn,state)
			else:
			    print("ignored transaction")
			    sys.stdout.flush()
			    continue

		myBlock = next_block(txnList,bchain)

		print("Blockchain on Node A is currently %s blocks long"%len(bchain))


		try:
			print("New Block Received; checking validity...")
			state = checkBlockValidity(myBlock,bchain[-1],state)
			bchain.append(myBlock)
		except:
			print("Invalid block; ignoring and waiting for the next block...")

		print("Blockchain on Node A is now %s blocks long"%len(bchain))


	print("\nThe chain contains - ")
	for nodes in bchain:
	    print("Block hash is: ", nodes['Hash'], "\n and Contents are: ", nodes['Contents'])