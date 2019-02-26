from solc import compile_source
from web3 import Web3
import os

def view_Details():
    provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../PrintNode/geth.ipc'))
    w3 = Web3(provider)

    with open('../contracts/Agreement.sol', 'r') as source_file:
        contract_source = source_file.read()

    compiled_sol = compile_source(contract_source)
    contract_interface = compiled_sol['<stdin>:Agreement']

    w3.eth.defaultAccount = w3.eth.accounts[0]

    contractAddress = input("Enter contract address: ")
    contractAddress = Web3.toChecksumAddress(Web3.toHex(hexstr = contractAddress))

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




