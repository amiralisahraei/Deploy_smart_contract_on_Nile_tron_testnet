from tronpy import Tron
from tronpy.keys import PrivateKey
from solcx import compile_source



client = Tron(network='nile')
priv_key = PrivateKey(bytes.fromhex(
    "3cb104ee7d6aeb9e05281c62c3c132d2719e2f76a488661699d9bb3e1b8c6b43"))



# connet to smart contract
created_cntr = client.get_contract('TYeSEortpAFtFnfWxLRfAke6TbARiszFzt')


# send a transaction
txn1 = (
    created_cntr.functions.setGreeting('Amirali')
    .with_owner('TXti8wxsj5EpvAQqPztmmQBfTc4mH4CnTB')
    .fee_limit(100_000_000)
    .build()
    .sign(priv_key)
)
result1 = txn1.broadcast().wait()

print(created_cntr.functions.greet.call())
