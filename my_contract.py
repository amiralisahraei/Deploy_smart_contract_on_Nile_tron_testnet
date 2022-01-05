from tronpy import Tron, Contract
from tronpy.keys import PrivateKey
from solcx import compile_source
from solidity_code import *


compiled_sol = compile_source(
    solidity_code, output_values=["abi", "bin"])


contract_id, contract_interface = compiled_sol.popitem()

# connect to Nile network
client = Tron(network='nile')
priv_key = PrivateKey(bytes.fromhex(
    "3cb104ee7d6aeb9e05281c62c3c132d2719e2f76a488661699d9bb3e1b8c6b43"))


cntr = Contract(name="Greeter", bytecode=contract_interface['bin'], abi=contract_interface['abi'])

# send transaction to deploy contract
txn = (
    client.trx.deploy_contract('TXti8wxsj5EpvAQqPztmmQBfTc4mH4CnTB', cntr)
    .fee_limit(90_000_000)
    .build()
    .sign(priv_key)
)
result = txn.broadcast().wait()

# print smart contract address
print(result['contract_address'])

