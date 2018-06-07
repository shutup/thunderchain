# -*- coding: utf-8 -*-
import requests
import hashlib
test_email = "your email"
//you can change
contract_bytecode = "0x608060405260405160208061025b83398101806040528101908080519060200190929190505050806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506101e5806100766000396000f300608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe014610067578063209652551461009257806355241077146100bd578063771602f7146100ea575b600080fd5b34801561007357600080fd5b5061007c610135565b6040518082815260200191505060405180910390f35b34801561009e57600080fd5b506100a7610154565b6040518082815260200191505060405180910390f35b3480156100c957600080fd5b506100e86004803603810190808035906020019092919050505061015e565b005b3480156100f657600080fd5b5061011f60048036038101908080359060200190929190803590602001909291905050506101ac565b6040518082815260200191505060405180910390f35b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000600154905090565b80600181905550803373ffffffffffffffffffffffffffffffffffffffff167f1b9a03d2a14aee4c88ec4b155f9b67023c06706b8fafa6321a716ef738f091f160405160405180910390a350565b60008183019050929150505600a165627a7a72305820d7a878a997c630fe377156d6a22673b6aee14bb09aa2cfb08325995290bf9d3e00290000000000000000000000007e74aeb1aa2bc2d5ebac5b0f4227434c7968f059"
//feel free to change
contract_params = "0x7e74aeb1aa2bc2d5ebac5b0f4227434c7968f059"
contract_abi = ""
//this is an deployed contract addr
contract_address = "0xa7010f333600fff3e3ac0cfe0cf31a8c0fe31d0a"

service_id = "your service_id"
secret = "your secret"

baseUrl = 'https://sandbox-walletapi.onethingpcs.com'
headers = {'content-type':'application/json','user-agent':'okhttp/3.3.1'}

def register(email,callback):
    payload = {
            "email":email,
            "callback":callback
            }
    r = requests.post(baseUrl+'/api/linktest/regist',headers = headers,json = payload)
    print(r.status_code)
    print(r.json())

def recharge(email,wallet_addr):
    signStr = md5("email={}&address={}&secret={}".format(email,wallet_addr,secret))
    payload = {
        "email":email,
        "address":wallet_addr,
        "sign":signStr
    }
    r = requests.post(baseUrl+'/api/linktest/recharge',headers = headers,json = payload)
    print(r.status_code)
    print(r.json())

def deploy(email,bytecode,params):
    payload = {
        "email":email,
        "bytecode" : bytecode,
        "params"  : params,
        "sign":md5("email={}&bytecode={}&params={}&secret={}".format(email,bytecode,params,secret))
    }
    r = requests.post(baseUrl+'/api/linktest/contract/deploy',headers = headers,json = payload)
    print(r.status_code)
    print(r.json())

def address(email,id):
    payload = {
        "email":email,
        "id":id,
        "sign":md5("email={}&id={}&secret={}".format(email,id,secret))
    }
    r = requests.post(baseUrl+'/api/linktest/contract/address',headers = headers,json = payload)
    print(r.status_code)
    print(r.json())

def last_contracts(email):
    payload = {
        "email":email,
        "sign":md5("email={}&secret={}".format(email,secret))
    }
    r = requests.post(baseUrl+'/api/linktest/contract/last',headers = headers,json = payload)
    print(r.status_code)
    print(r.json())


def tx_generate(email,to,value,callback,title,desc,gas_limit,data,tx_type):
    payload = {
        "email":email,
        "to": to,
        "value":value,
        "callback":callback,
        "title":title,
        "desc":desc,
        "gas_limit":gas_limit,
        "data": data,
        "tx_type":tx_type,
        "sign":md5("email={}&to={}&value={}&secret={}".format(email,to,value,secret))
    }
    r = requests.post(baseUrl+"/api/linktest/tx_generate",headers = headers,json = payload)
    print(r.status_code)
    print(r.json())

def md5(content):
    m = hashlib.md5()
    m.update(content.encode('utf-8'))
    signStr = m.hexdigest()
    return signStr


#register("fyjc999@gmail.com", "test")
# recharge("fyjc999@gmail.com", "0x7e74aeb1aa2bc2d5ebac5b0f4227434c7968f059")
# deploy(test_email, contract_bytecode, contract_params)
#id :10741
# address(test_email, 10741)
tx_generate(test_email,contract_address, "0", "http://baidu.com","test title","test desc","100000","0x552410770000000000000000000000000000000000000000000000000000000000000002","contract");
#contract_address:0xa7010f333600fff3e3ac0cfe0cf31a8c0fe31d0a

# curl -k -X POST -H "Content-Type:application/json" --data '{"jsonrpc":"2.0","method":"eth_call","params":[{"from":"0x7eff122b94897ea5b0e2a9abf47b86337fafebdc","to":"0xa7010f333600fff3e3ac0cfe0cf31a8c0fe31d0a","data":"0x771602f70000000000000000000000000000000000000000000000000000000000000017000000000000000000000000000000000000000000000000000000000000002d"}, "latest"],"id":1}' https://sandbox-walletapi.onethingpcs.com/call
#
# curl -k -X POST -H "Content-Type:application/json" --data '{"jsonrpc":"2.0","method":"eth_call","params":[{"from":"0x7eff122b94897ea5b0e2a9abf47b86337fafebdc","to":"0xa7010f333600fff3e3ac0cfe0cf31a8c0fe31d0a","data":"0x20965255"}, "latest"],"id":1}' https://sandbox-walletapi.onethingpcs.com/call
# {"jsonrpc":"2.0","id":1,"result":"0x0000000000000000000000000000000000000000000000000000000000000000"}
