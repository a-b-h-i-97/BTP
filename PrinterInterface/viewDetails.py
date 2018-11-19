from solc import compile_source
from web3 import Web3

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from contract_source import contract_sc

provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../PrintNode/geth.ipc'))
w3 = Web3(provider)

compiled_sol = compile_source(contract_sc)
contract_interface = compiled_sol['<stdin>:Agreement']

w3.eth.defaultAccount = w3.eth.accounts[0]

contractAddress = input("Enter contract address: ")
contractAddress = Web3.toChecksumAddress(Web3.toHex(hexstr = contractAddress))

# passphrase = input("Enter passphrase: ")
# w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)

Agreement = w3.eth.contract(
    address = contractAddress,
    abi=contract_interface['abi'],
)

quantity = Agreement.functions.QUANTITY().call()
amount = Agreement.functions.amount().call()
balance = Agreement.functions.getBalance().call()
quantityRemaining = Agreement.functions.quantityRemaining().call()

print("Quantity: ", quantity)
print("Amount: ", amount)
print("Balance: ", balance)
print("Quantity Remaining ", quantityRemaining)




