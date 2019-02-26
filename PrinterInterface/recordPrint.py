from solc import compile_source
from web3 import Web3
import getpass
import os

def record_print():
    provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../PrintNode/geth.ipc'))
    w3 = Web3(provider)

    with open('../contracts/Agreement.sol', 'r') as source_file:
        contract_source = source_file.read()

    compiled_sol = compile_source(contract_source)
    contract_interface = compiled_sol['<stdin>:Agreement']

    w3.eth.defaultAccount = w3.eth.accounts[0]

    contractAddress = input("Enter contract address: ")
    contractAddress = Web3.toChecksumAddress(Web3.toHex(hexstr = contractAddress))

    designID = input("Enter designID: ")

    passphrase = getpass.getpass("Enter passphrase: ")
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)

    Agreement = w3.eth.contract(
        address=contractAddress,
        abi=contract_interface['abi'],
    )

    try:
        tx_hash = Agreement.functions.recordPrint(designID).transact()

    except ValueError:
        print("Unauthorized printer or agreement has ended")
        return

    print("Waiting for transaction to be mined...")
    w3.eth.waitForTransactionReceipt(tx_hash)

    quantityRemaining = Agreement.functions.quantityRemaining().call()

    print("Print record successful!! \n Quantity remaining as per agreement: ", quantityRemaining)