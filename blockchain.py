import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.chain.append(new_block)

    def get_balance(self, user):
        balance = {}
        for block in self.chain:
            for txn in block.transactions:
                if txn["sender"] == user:
                    balance[txn["coin"]] = balance.get(txn["coin"], 0) - txn["amount"]
                if txn["receiver"] == user:
                    balance[txn["coin"]] = balance.get(txn["coin"], 0) + txn["amount"]
        return balance

    def get_transactions(self, user):
        txns = []
        for block in self.chain:
            for txn in block.transactions:
                if txn["sender"] == user or txn["receiver"] == user:
                    txns.append(txn)
        return txns
