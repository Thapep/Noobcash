# Should import blockchain?
# import blockchain
import datetime
import json
from Crypto.Hash import SHA256
import jsonpickle

class Block:
	def __init__(self, myid, previousHash=0, listOfTransactions=[], current_hash=None, nonce=0):
		##set
		# nonce = 0 only if we dont give any argument 
		self.myid = myid
		self.previousHash = previousHash
		self.timestamp = str(datetime.datetime.utcnow())
		self.current_hash = current_hash   
		self.nonce = nonce 
		self.capacity = 5
		self.listOfTransactions = listOfTransactions

	def myHash(self):
		return (SHA256.new(self.dump().encode()).hexdigest())

	def add_transaction(self, transaction):
		if len(self.listOfTransactions) < self.capacity:
			print("In add_transaction if: ")
			print(self.listOfTransactions)
			self.listOfTransactions.append(transaction)
			print(self.listOfTransactions)

	def dump(self):
		# Structure with trans, nonce, timestamp to use them in calculation of hash
		transactions_pickle = jsonpickle.encode(self.listOfTransactions)
		return json.dumps(dict(transactions=transactions_pickle,nonce=self.nonce,timestamp=self.timestamp), sort_keys=True)

