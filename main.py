import hashlib

class JonCoin:
    def __init__(self, previous_block_hash='0', transaction_list=None):
        '''This blockchain constructor will create a block'''
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list or ['First Block']
        self.block_data = "-".join(self.transaction_list) + "-" + self.previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def __str__(self):
        return f"Block Data: {self.block_data}\nBlock Hash: {self.block_hash}\n"

# Create the initial block
initial_block = JonCoin()
print(initial_block)

# List to store the blockchain
blockchain = [initial_block]

mainloop = True
while mainloop:
    print("Enter a new transaction (or 'quit' to exit):")
    new_transaction = input()

    if new_transaction.lower() == 'quit':
        mainloop = False
        continue

    # Add the new transaction to the list
    transactions = [new_transaction]

    # Get the previous block's hash
    previous_block_hash = blockchain[-1].block_hash

    # Create a new block
    current_block = JonCoin(previous_block_hash, transactions)

    # Add the new block to the blockchain
    blockchain.append(current_block)

    # Print the new block's details
    print(current_block)
