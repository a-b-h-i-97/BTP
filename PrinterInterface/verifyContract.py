from solc import compile_source
from web3 import Web3
import os

def verify_contract():
    provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../PrintNode/geth.ipc'))
    w3 = Web3(provider)

    with open('../contracts/Agreement.sol', 'r') as source_file:
        contract_source = source_file.read()

    compiled_sol = compile_source(contract_source)
    contract_interface = compiled_sol['<stdin>:Agreement']

    w3.eth.defaultAccount = w3.eth.accounts[0]

    tx_hash = input("Enter transaction hash: ")
    tx = w3.eth.getTransaction(tx_hash)

    input_data = tx['input'][2: ]
    input_data = input_data[0: len(contract_interface['bin'])]

    if(input_data == contract_interface['bin']):
        print("Contract byte code matches compiled byte code")
    else:
        print("Contract byte code does not match compiled byte code")
        print(input_data)
        print(contract_interface['bin'])