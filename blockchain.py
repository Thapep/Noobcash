import block
#import transaction
#import wallet 

class Blockchain:

    def __init__(self):
        self.chain = []

    def add_block(self, block):

        self.chain.append(block)  
        return True

    def last_block(self):
        return self.chain[-1]

    def view_transactions(self):
        #prints the transactions of the last block
        last_transactions = self.last_block().listOfTransactions
        for i in range(len(last_transactions)):
            print(last_transactions[i])

    def print_chain(self):
        i = 0
        for bentry in self.chain:
            print('=======')
            print("Block ", i,)
            transactions = bentry.listOfTransactions
            j = 0
            for tentry in transactions:
                print('\t',j,': ',tentry.index)
                j +=1
            i += 1        
