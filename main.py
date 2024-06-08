import hashlib

class JonCoin:

    def __init__(self, previous_block_hash = '0', transaction_list = 'First Block'):
        '''This blockchain constructor which will create the first block'''
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() 




inital_block = JonCoin()
print(inital_block.block_data)
print(inital_block.block_hash)