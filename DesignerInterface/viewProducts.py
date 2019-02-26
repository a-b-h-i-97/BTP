from solc import compile_source
from web3 import Web3
import os


def view_products():

    provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../DesignNode/geth.ipc'))
    w3 = Web3(provider)
    
    with open('../contracts/Agreement.sol', 'r') as source_file:
        contract_source = source_file.read()

    compiled_sol = compile_source(contract_source)
    contract_interface = compiled_sol['<stdin>:Agreement']

    w3.eth.defaultAccount = w3.eth.accounts[0]

    contractAddress = input("Enter contract address: ")
    contractAddress = Web3.toChecksumAddress(Web3.toHex(hexstr = contractAddress))

    Agreement = w3.eth.contract(
        address=contractAddress,
        abi=contract_interface['abi'],
    )

    quantity = Agreement.functions.QUANTITY().call()
    quantityRemaining = Agreement.functions.quantityRemaining().call()
    quantityPrinted = quantity - quantityRemaining

    print("Number of products printed: ", quantityPrinted)

    i = 0
    while(i < quantityPrinted):
        product = Agreement.functions.products(i).call()
        print(product)
        i = i+1
    
