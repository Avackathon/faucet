from fastapi import FastAPI
from web3 import Web3

import os

# env variables
network_rpc = os.getenv("NETWORK_RPC", "https://api.avax-test.network/ext/bc/C/rpc")

# connect to the network
web3 = Web3(Web3.HTTPProvider(network_rpc))

# SubNav subnet prefunded account
account_1 = '0x8db97C7cEcE249c2b98bDC0226Cc4C2A57BF52FC'
private_key1 = '56289e99c94b6912bfc12adc093c9b51124f0dc54ac7a766b2bc5ccf558d8027'

# start FastAPI
app = FastAPI()

# faucet endpoint
@app.put("/faucet/{address}")
async def fund_wallet(address: str):
    # get the nonce.  Prevents one from sending the transaction twice
    nonce = web3.eth.getTransactionCount(account_1)

    # build a transaction in a dictionary
    tx = {
        'chainId': 13213,
        'nonce': nonce,
        'to': address,
        'value': web3.toWei(10, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }

    # sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

    # send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # return transaction hash
    return { web3.toHex(tx_hash) }
