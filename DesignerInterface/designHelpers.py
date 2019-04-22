from solc import compile_source
from web3 import Web3
import getpass
from py_essentials import hashing as hs
import os

provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../DesignNode/geth.ipc'))
w3 = Web3(provider)

def create_contract_object(w3):
    with open('../contracts/Designdb.sol', 'r') as source_file:
        contract_source = source_file.read()

    compiled_sol = compile_source(contract_source)
    contract_interface = compiled_sol['<stdin>:DesignDB']

    w3.eth.defaultAccount = w3.eth.accounts[0]
    
    contractAddress = input("Enter contract address: ")
    contractAddress = Web3.toChecksumAddress(Web3.toHex(hexstr = contractAddress))

    designDb = w3.eth.contract(
        address = contractAddress,
        abi = contract_interface['abi'],
    )
    return designDb


def upload_design(w3):
    designDb = create_contract_object(w3)
    filePath = input("Enter filepath: ")
    fileHash = hs.fileChecksum(filePath,'sha256',True)
    filesLength = designDb.functions.getFilesLength().call()
    print("Files Length",filesLength)

    fileName = input("Enter filename")
    version = input("Enter version")
    passphrase = getpass.getpass("Enter passphrase: ")
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)
 
    tx_hash = designDb.functions.addDesign(fileName,fileHash,version).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    print("Transaction mined. TX Hash:",Web3.toHex(tx_hash)) 
    newFilesLength = designDb.functions.getFilesLength().call()
    if(newFilesLength == filesLength):
        print("Design not uploaded(fileHash)")
    else:
        print("Design uploaded successfully")
    

    
def get_files_length(w3):
    designDb = create_contract_object(w3)
    filesLength = designDb.functions.getFilesLength().call()
    print("Files Length:",filesLength)



def get_design(w3):
    designDb = create_contract_object(w3)
    filePath = input("Enter filepath: ")
    fileHash = hs.fileChecksum(filePath,'sha256',True)
    index = designDb.functions.findDesign(fileHash).call()
    if (index==-1):
        print("No results")
        return 
    design = designDb.functions.getDesign(index).call()
    print("Designer:",design[0])
    print("Filename:",design[1])
    print("Filehash:",design[2])
    print("Version:",design[3])
    print("Timestamp:",design[4])
    historyLen = designDb.functions.getHistoryLength(index).call()
    for i in range(historyLen):
        version = designDb.functions.getHistory(index,i).call()
        print("Version:",version[0])
        print("FileHash:",version[1])
        print("Timestamp:",version[2])
    
def update_design(w3):
    designDb = create_contract_object(w3)
    filePath = input("Enter filepath:")
    fileHash = hs.fileChecksum(filePath,'sha256',True)
    index = designDb.functions.findDesign(fileHash).call()
    if (index == -1):
        print("No results")
        return
    newFilePath = input("Entere new filepath:")
    newFileHash = hs.fileChecksum(newFilePath,'sha256',True)
    version = input("Enter version")
    
    passphrase = getpass.getpass("Enter passphrase:")
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)

    tx_hash = designDb.functions.modifyDesign(index,newFileHash,version).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("Transaction mined. TX Hash:",Web3.toHex(tx_hash))
    design = designDb.functions.getDesign(index).call()
    if(design[2] != newFileHash):
        print("Design not update(designe with same hash exists)")
    else:
        print("Design updated")
    
def kill():
    designDb = create_contract_object(w3)
    passphrase = getpass.getpass("Enter passphrase:")
    w3.personal.unlockAccount(w3.eth.accounts[0], passphrase)
    designDb.functions.kill().tranasct()

# # upload_design(w3)
# get_files_length(w3)
# get_design(w3)
# # update_design(w3)


