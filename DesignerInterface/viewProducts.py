from solc import compile_source
from web3 import Web3

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from contract_source import contract_sc

provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../DesignNode/geth.ipc'))
w3 = Web3(provider)

def view_products():
    compiled_sol = compile_source(contract_sc)
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
    
