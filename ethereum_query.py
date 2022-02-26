from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#    print( "Connected to Ethereum node" )
    pass
else:
    print( "Failed to connect to Ethereum node!" )



def get_transaction(tx):
    tx = {}   #YOUR CODE HERE
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    tx = w3.eth.get_transaction(tx)
    gas_price = tx['gasPrice']
    return gas_price

def get_gas(tx):
    tx = w3.eth.get_transaction_receipt(tx)
    gas = tx['gasUsed']
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas(tx)*get_gas_price(tx)
    return tx_cost

def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    for tx in block['transactions']:
        block_cost += get_transaction_cost(tx)
    
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    block = w3.eth.get_block(block_num)
    max_tx_cost = 0
    for tx in block['transactions']:
        tx_cost = get_transaction_cost(tx)
        if tx_cost > max_tx_cost
            max_tx = tx
            max_tx_cost = tx_cost
    
    return max_tx

