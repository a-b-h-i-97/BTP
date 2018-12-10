from solc import compile_source
from web3 import Web3
import getpass

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from contract_source import contract_sc

def create_contract():
    provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../DesignNode/geth.ipc'))
    w3 = Web3(provider)


    compiled_sol = compile_source(contract_sc)
    contract_interface = compiled_sol['<stdin>:Agreement']

    w3.eth.defaultAccount = w3.eth.accounts[0]

    Agreement = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    quantity = input("Enter agreement quantity: ")
    quantity = int(quantity)

    amount = input("Enter agreement amount: ")
    amount = int(amount)

    passphrase = getpass.getpass("Enter passphrase: ")

    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)

    tx_hash = Agreement.constructor(quantity, amount).transact()
    print("\nTransaction hash: ", Web3.toHex(tx_hash))

    print("Waiting for transaction to be mined...")
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    print("Contract successfully deployed!!")
    print("Contract address: ", tx_receipt.contractAddress)
    
    return



