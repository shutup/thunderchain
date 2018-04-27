
# 迅雷全球区块链应用大赛开发指南

- [迅雷全球区块链应用大赛开发指南](#)
	- [合约开发入门线路推荐](#)
	- [基本概念](#)
		- [区块链(Blockchain)](#blockchain)
		- [交易(Transaction)](#transaction)
		- [账户(Account)](#account)
		- [合约(Contract)](#contract)
		- [Gas](#gas)
		- [Solidity](#solidity)
		- [注意事项](#)
	- [使用truffle 开发合约](#truffle)
		- [安装truffle](#truffle)
		- [开始](#)
	- [使用truffle unbox创建可交互合约应用](#truffle-unbox)
	- [使用浏览器插件 metamask 与区块链交互](#metamask)
	- [参赛者提交文件说明](#)

## 合约开发入门线路推荐
1. 在编写智能合约前，需要对[区块链基础](http://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html#blockchain-basics)有一定的了解(附：[ethereum-overview](http://truffleframework.com/tutorials/ethereum-overview))。
2. 学习solidity语言 ([solidity API](http://solidity.readthedocs.io/en/v0.4.21/index.html))。
3. 结合solidity的学习，学习使用 [truffle 框架](http://truffleframework.com/docs) 。使用truffle develop在本地区块链环境下运行合约。
4. 学习和使用[zeppelin-solidty (致力于安全的标准化的合约框架)](https://openzeppelin.org/)  ，设计合约模式，分离数据和逻辑合约，控制权限安全，考虑升级逻辑。
5. 学习使用 [web3.js](http://web3js.readthedocs.io/en/1.0/index.html)与合约交互。使用Metamask插件和web服务与区块链交互。
6. **论坛答疑：http://wanke.xunlei.com/forum.php?mod=forumdisplay&fid=53 （您碰到的任何问题，都可在此论坛反馈，我们将在3个工作日内给您回复）**

## 基本概念
### 区块链(Blockchain)
区块链是一种去中心化的分布式计算系统，主要的特点是数据永久不可篡改性、不可伪造、公开透明信任度高。核心的技术包括拜占庭容错的共识算法(PBFT)、加密技术、P2P技术等。

### 交易(Transaction)
区块链可以理解为一个全局共享的交易数据库系统。任何有权限的软件都可以读取区块链网络中的数据。当需要改变区块网络中的数据时，就必须发起一个被所有区块节点接受的请求，这个请求在系统中统称为交易(Transaction)。   
交易具有事务性，提交到区块链，要么全部不执行，要么全部执行。一个交易执行完成后永久保存到区块链，不能再做修改和再次执行。   
交易由系统中的账户(Account)发起并且签名，通过加密技术，交易只能由私钥持有人发起，其他人不能修改和伪造。这样保证了交易的真实和安全。

### 账户(Account)
在区块链系统中有两类账户，一个是外部账户，一个是合约账户。外部账户拥有自己独有的公私密钥，账户由这个密钥对控制。合约账户有自己的代码，账户由自己的代码控制。   
账户由一个地址标识，地址长度是一样的，两类账户无差别。外部账户的地址由其公钥产生，合约地址使用创建合约账户的地址以及创建合约账户的交易数(nonce)产生。合约由官方地址统一部署，普通账户不能直接发布合约。用户的合约必须经过官方评审，由迅雷统一发布。   
在系统内部，对待这两类账户是无差别的。每个账户在系统内部有一个256bits到256bits的key-value存储结构，叫做storage。每个账户有个余额叫做balance，单位是wei，可以通过发送带数值的交易到账户进行修改。

### 合约(Contract)
合约就是存储了代码的区块链账户，通过给这个账户发送交易实现合约调用。当前比较流行的合约编程语言是Solidity。当前大赛只支持Solidity语言提交合约。   
合约内部分为两个部分，数据储存和函数，数据存储着合约的状态，函数是合约对外的接口，通过调用函数实现数据查询和状态修改。   
通过编程语言书写合约，编译后得到EVM字节码。通过给合约账户发送交易，实现合约调用。

### Gas
Gas是区块链的付费单位，一个交易创建的时候，会指定支付一定数量的Gas。主要是为了约束交易的运算量，以及为交易执行支付费用。交易执行过程中，Gas会以一个EVM设定的规则消耗。   
Gas价格(Gas price)是由交易创建者指定的一个值，交易执行需要支付的费用数量为Gas_Price*Gas。交易结束如果Gas有剩余，剩余部分会返回给创建建议的用户。如果Gas不足，交易执行会失败，为了系统安全防止泛洪攻击，交易失败的手续费不返回。Gas价格的最小单位是wei，10^18 wei = 1 链克。


### Solidity
Solidity是针对智能合约设计的一门高级编程语言，运行环境是EVM(Ethereum Virtual Machine)。语言设计实现中受到了C++/Python/JavaScript的影响。Solidity是强类型语言，支持继承、多态、接口、抽象、库、自定义数据类型等特性。Solidity支持汇编指令编程，代码编译为字节码后运行在EVM上。Solidity是当下最流行的智能合约开发语言,也是迅雷合约平台推荐和支持的语言。

### 注意事项
1. Ethereum Virtual Machine 是在以太坊上为智能合约提供运行时环境的虚拟机。大赛平台兼容EVM，但需遵循官方平台的使用约束。
1. 账户类型分为外部账户（普通的交易账户地址）和合约账户。创建合约就是向目标账户地址0发送交易的过程。
1. **大赛指定使用truffle（truffle v4.1.5 solidity v0.4.21）开发智能合约，平台方会根据参赛者提交的文件源码校验bytecode。**，

## 使用truffle 开发合约
> 智能合约solidity开发框架[truffle](http://truffleframework.com/docs/)。
> 提供了一套完善的开发、调试、编译、部署、测试的本地环境。
> 可以使用模板命令unbox根据一些模板快速生成对应的合约架构。

### 安装truffle 

	npm i -g truffle 

	[root@opennode sandai]# truffle version
	Truffle v4.1.5 (core: 4.1.5)
	Solidity v0.4.21 (solc-js)

### 开始
1. 使用truffle 初始化合约工程

		mkdir simple-storage
		cd simple-storage
		truffle init

2. 新建合约文件：可以使用 `truffle create contract SimpleStorage` 命令行新建，也可以直接新建文件 contract/SimpleStorage.sol

		// SimpleStorage.sol
		pragma solidity ^0.4.21;
		contract SimpleStorage {
			uint myVariable; 

			function set(uint x) public {
				myVariable = x;
			}

			function get() constant public returns (uint) {
				return myVariable;
			} 
		}
3. 添加migrate脚本：可以使用`truffle create migration 2_deploy_contract` 命令行方式新增，也可以直接新建文件 migrations/2_deploy_contract.js

		// 2_deploy_contract.js；truffle migrate命令的执行顺序与文件名有关，所以多个部署脚本需要按照顺序命名
		var SimpleStorage = artifacts.require("SimpleStorage");
		module.exports = function(deployer) {
				deployer.deploy(SimpleStorage);
		}; 

4. 执行truffle compile编译合约，编译后的合约在build文件夹下。每个合约有一个对应的json文件，内含部署所需的bytecode,abiCode等
5. 编辑 truffle.js ，设置truffle部署合约及与区块链交互的rpc连接。

		[root@localhost opennode]# vi truffle.js 
		module.exports = {
			networks: {
				development: {
					host: "127.0.0.1",
					port: 8545, 
					network_id: "*"
				}
			}
		};
6. 控制台开启truffle默认的区块链环境。

		truffle develop
		Truffle Develop started at http://127.0.0.1:9545/

		Accounts:
		(0) 0x627306090abab3a6e1400e9345bc60c78a8bef57
		(1) 0xf17f52151ebef6c7334fad080c5704d77216b732
		(2) 0xc5fdf4076b8f3a5357c5e395ab970b5b54098fef
		(3) 0x821aea9a577a9b44299b9c15c88cf3087f3b5544
		(4) 0x0d1d4e623d10f9fba5db95830f7d3839406c6af2
		(5) 0x2932b7a2355d6fecc4b5c0b6bd44cc31df247a2e
		(6) 0x2191ef87e392377ec08e7c08eb105ef5448eced5
		(7) 0x0f4f2ac550a1b4e2280d04c21cea7ebd822934b5
		(8) 0x6330a553fc93768f612722bb8c2ec78ac90b3bbc
		(9) 0x5aeda56215b167893e80b4fe645ba6d5bab767de

		Private Keys:
		(0) c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3
		(1) ae6ae8e5ccbfb04590405997ee2d52d2b330726137b875053c36d94e974d162f
		(2) 0dbbe8e4ae425a6d2687f1a7e3ba17bc98c673636790f1b8ad91193c05875ef1
		(3) c88b703fb08cbea894b6aeff5a544fb92e78a18e19814cd85da83b71f772aa6c
		(4) 388c684f0ba1ef5017716adb5d21a053ea8e90277d0868337519f97bede61418
		(5) 659cbb0e2411a44db63778987b1e22153c086a95eb6b18bdf89de078917abc63
		(6) 82d052c865f5763aad42add438569276c00d3d88a2d062d36b2bae914d58b8c8
		(7) aa3680d5d48a8283413f7a108367c7299ca73f553735860a87b08f39395618b7
		(8) 0f62d96d6675f32685bbdb8ac13cda7c23436f63efbb9d07700d8669ff12b7c4
		(9) 8d5366123cb560bb606379f90a0bfd4769eecc0557f1b362dcae9012b548b1e5

		Mnemonic: candy maple cake sugar pudding cream honey rich smooth crumble sweet treat

		⚠️  Important ⚠️  : This mnemonic was created for you by Truffle. It is not secure.
		Ensure you do not use it on production blockchains, or else you risk losing funds.

		truffle(develop)>
		
	这为truffle运行合约提供了本地的区块链环境，默认生成10个账户，每个账户初始余额为100ether。
	也可以使用[Ganache](http://truffleframework.com/ganache/)提供的图形化界面应用，需要修改配置连接的端口。
7. 在一个新的控制台执行truffle migrate移植部署合约（或者在truffle develop控制台执行 migrate）。
8. 使用truffle develop测试合约代码。

		SimpleStorage.deployed().then(function(instance){return instance.get.call();}).then(function(value){return value.toNumber()})
		// 0
		SimpleStorage.deployed().then(function(instance){return instance.set(100);});
		// 输出transaction信息
		SimpleStorage.deployed().then(function(instance){return instance.get.call();}).then(function(value){return value.toNumber()});
		// 100
9. 使用truffle test 测试合约
	使用truffle create test SimpleStorage新建或直接新建文件test/SimpleStorage.test.js。

		const SimpleStorage = artifacts.require('SimpleStorage');

		contract('SimpleStorage', function(accounts) {
			it("should assert true", function(done) {
				var simpleStorage = SimpleStorage.deployed();
				var instance;
				simpleStorage.then(res => {
					instance = res;
					return instance.get()
				}).then(value => {
					assert.equal('0', value.toNumber(), 'not equal 0')
				}).then(() => {
					instance.set(100)
				}).then(() => {
					return instance.get()
				}).then(value => {
					assert.equal('100', value.toNumber(), 'not equal 100')
				})
				done();
			});
		});

	在新开的控制台里，输入truffle test ./test/SimpleStorage.test.js。

10. 使用remix测试合约
将使用truffle 开发的合约，放在[remix](http://remix.ethereum.org/)里，可快速模拟合约的部署和调用。
remix提供了合约的编译运行环境，并可以在控制台看到合约每条交易的详细信息，如输入输出参数，签名后的方法data，交易hash等信息。支持调试。

	1. 使用compile detail，可以看到合约编译详情。包括bytecode，abi和使用web3.js快速部署的滴啊用方法。
	![图片1.png](https://upload-images.jianshu.io/upload_images/8918886-75d904d5f3a0f866.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

	2. 使用run来create 合约，控制台可查看创建合约的交易。
	![图片.png](https://upload-images.jianshu.io/upload_images/8918886-c01f8b9021e6ce3d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 使用truffle unbox创建可交互合约应用
上面的步骤使用基本的truffle init创建了一个可编译部署调试的合约环境。
下面使用truffle unbox创建一个新的工程，unbox为我们提供了truffle工程模板，内置了一些合约应用交互的环境依赖。
可以在[truffle boxes](http://truffleframework.com/boxes/)里查看官方提供的各种模板boxes。
下面使用的是react模板.

1. 新建工程 truf-react

		mkdir truf-react
		cd truf-react
		truffle unbox react

	unbox过程会下载解压模板，执行npm install等操作。
2. 配置项目的truffle.js

		module.exports = {
			// See <http://truffleframework.com/docs/advanced/configuration>
			// to customize your Truffle configuration!
			networks: {
				development: {
					host: '127.0.0.1',
					port: '9545',
					network_id: '*' // Match any network id
				}
			}
		};

3. 启动一个truffle develop
4. 修改src/App.js

		import React, { Component } from 'react'
		import SimpleStorageContract from '../build/contracts/SimpleStorage.json'
		import getWeb3 from './utils/getWeb3'

		import './css/oswald.css'
		import './css/open-sans.css'
		import './css/pure-min.css'
		import './App.css'

		const contract = require('truffle-contract')
		const simpleStorage = contract(SimpleStorageContract)

		class App extends Component {
			constructor(props) {
				super(props)

				this.state = {
					storageValue: 0,
					web3: null,
					inputValue: 0,
					address: null
				}

				this.changeValueHandle = this.changeValueHandle.bind(this)
				this.setHandle = this.setHandle.bind(this)
			}

			componentWillMount() {
				// Get network provider and web3 instance.
				// See utils/getWeb3 for more info.

				getWeb3
				.then(results => {
					this.setState({
						web3: results.web3
					})

					// Instantiate contract once web3 provided.
					this.instantiateContract()
				})
				.catch(() => {
					console.log('Error finding web3.')
				})
			}

			instantiateContract() {
				/*
				* SMART CONTRACT EXAMPLE
				*
				* Normally these functions would be called in the context of a
				* state management library, but for convenience I've placed them here.
				*/

				this.simpleStorageSet(5)
			}

			changeValueHandle(event) {
				this.setState({
					inputValue: Number(event.target.value)
				})
			}

			setHandle() {
				this.simpleStorageSet(this.state.inputValue)
			}

			simpleStorageSet(x) {
				simpleStorage.setProvider(this.state.web3.currentProvider)

				// Declaring this for later so we can chain functions on SimpleStorage.
				var simpleStorageInstance

				// Get accounts.
				this.state.web3.eth.getAccounts((error, accounts) => {
					simpleStorage.deployed().then((instance) => {
						simpleStorageInstance = instance
						this.setState({ address: instance.address })
						// Stores a given value, 5 by default.
						return simpleStorageInstance.set(x, {from: accounts[0]})
					}).then((result) => {
						// Get the value from the contract to prove it worked.
						return simpleStorageInstance.get.call(accounts[0])
					}).then((result) => {
						// Update state with the result.
						return this.setState({ storageValue: result.c[0] })
					})
				})
			}

			render() {
				return (
					<div className="App">
						<nav className="navbar pure-menu pure-menu-horizontal">
								<a href="#" className="pure-menu-heading pure-menu-link">Truffle Box</a>
						</nav>

						<main className="container">
							<div className="pure-g">
								<div className="pure-u-1-1">
									<h1>Good to Go!</h1>
									<p>Your Truffle Box is installed and ready.</p>
									<h2>Smart Contract Example</h2>
									<p>If your contracts compiled and migrated successfully, below will show a stored value of 5 (by default).</p>
									<p>Try changing the value stored on <strong>line 59</strong> of App.js.</p>
									<p>The stored value is: {this.state.storageValue}</p>
									<p>deployed contract address: {this.state.address}</p>
								</div>
								<div>
									<input type="number" onChange={this.changeValueHandle}/>
									<button onClick={this.setHandle}>set</button>
								</div>
							</div>
						</main>
					</div>
				);
			}
		}

		export default App

	新增了合约set方法的调用。并展示了合约的address。
4. 新打开一个控制台，执行 npm run start 
5. 浏览器打开 http://lcoalhost:3000，可看到合约的结果。
7. 通过set和输入框设置合约storedData的值。
6. 在trufle develop里输入

		//将xxx替换为address
		SimpleStorage.at('xxxx').then(res => {return res.get()})
		// 得到BigNUmber类型的返回值，c数组里的值即为设置的storedData的值。

## 使用浏览器插件 metamask 与区块链交互
参考http://truffleframework.com/tutorials/pet-shop

## 参赛者提交文件说明
大赛指定使用truffle 开发智能合约，truffle 版本为 v4.1.5，对应的solcjs版本为 v0.4.21。
开发者需要提交truffle工程压缩包和相关项目介绍文档，至少包含以下内容：
1. truffle 工程基本文件结构:
	build
	contracts
	migrations
	test
	package.json
	truffle.js
	truffle-config.js
	README.md // 工程文档说明
	不需要node_modules
2. 需要提供整个项目产品的PPT或PDF讲解，内含产品背景介绍，产品意义，App下载地址（可选），产品使用流程介绍。

**后续第三方开发者可根据即将开放的迅雷链指引文档，实现合约应用与链克口袋交互。**

> 文档与工具  
> [solidity API](http://solidity.readthedocs.io/en/v0.4.21/index.html)  
> [truffle文档](http://truffleframework.com/docs)  
> [ganache 提供本地区块链环境的图形化界面](http://truffleframework.com/ganache/)  
> [zeppelin-solidty 致力于安全的标准化的合约框架](https://openzeppelin.org/)  
> [MetaMask 通过RPC连接为浏览器提供区块链环境的浏览器插件](https://metamask.io/)  
> [web3.js 以太坊封装的与区块链交互的js](http://web3js.readthedocs.io/en/1.0/index.html)  