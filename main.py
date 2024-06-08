import hashlib

class JonCoin:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() 


t1 = "Anna sends 2 NC to Mike"
t2 = "Dave sends 2 NC to Mike"
t3 = "Simon sends 2 NC to Mike"
t4 = "Paul sends 2 NC to Mike"
t5 = "Anna sends 2 NC to Mike"

inital_block = JonCoin('inital message', [t1, t2, t3, t4, t5])
print(inital_block.block_data)
print(inital_block.block_hash)