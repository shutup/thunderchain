pragma solidity ^0.4.18;

//owner: 0x7e74aeb1aa2bc2d5ebac5b0f4227434c7968f059
//id :10741
contract SimpleStorage {
    address owner;
    uint storedData;
  event SET(address indexed _addr,uint indexed _value);

  constructor (address onwerAddr) public payable{
      owner=onwerAddr;
  }

  function setValue(uint x) public {
    storedData = x;
    emit SET(msg.sender,x);
  }

  function getValue() public view returns (uint) {
    return storedData;
  }

  function getBalance() public view returns(uint) {
      return address(this).balance;
  }

  function add(uint x,uint y) public pure returns(uint){
      return x+y;
  }

}
