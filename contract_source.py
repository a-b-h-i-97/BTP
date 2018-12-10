contract_sc = '''

pragma solidity >=0.4.22 < 0.6.0;

contract Agreement {

    address public designer;
    address public printer;

    uint public QUANTITY;
    uint public quantityRemaining;
    uint public amount;
    Product[] public products;
    
    struct Product {
        string id;
        uint time;
    }

    event Credit(address designer,uint amount,uint quantity,uint q_remain);
    event Debit(address designer,uint amount,uint quantity,uint q_remain);

    constructor (uint _QUANTITY, uint _amount) public {
        designer = msg.sender;
        QUANTITY = _QUANTITY;
        quantityRemaining = _QUANTITY;
        amount = _amount;        
    }

    modifier designeronly() {require(msg.sender==designer, "Only creator is authorized to do this operation"); _;}

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
    
    function () public payable designeronly {
        require(msg.value >= amount, "Cannot credit an amount less than agreed upon amount");

        emit Credit(msg.sender,amount,QUANTITY,quantityRemaining);
        
    }

    function registerPrinter() public {
        require(printer == 0x0, "This agreement already has a printer");
        require(address(this).balance >= amount, "Insufficient balance in contract account");
        
        printer = msg.sender;
    }

    function recordPrint(string designid) public {
        require(quantityRemaining > 0, "No more copies can be authenticated");
        require(msg.sender == printer, "Not authorized to print");

        quantityRemaining--;

        products[products.length++] = Product({id:designid, time:block.timestamp});
        if (quantityRemaining==0) {
            printer.transfer(amount);
        }

        emit Debit(printer,amount,QUANTITY,quantityRemaining);        
    }
}

'''