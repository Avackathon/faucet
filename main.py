from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web3 import Web3

import os

# env variables
network_rpc = os.getenv("NETWORK_RPC", "https://api.avax-test.network/ext/bc/C/rpc")

# connect to the network
web3 = Web3(Web3.HTTPProvider(network_rpc))

# Read SubNav subnet prefunded account's keys
with open("files/account.pub") as f:
    account_1 = f.read().replace('\n', '')
with open("files/account.key") as f:
    private_key1 = f.read().replace('\n', '')

# start FastAPI
app = FastAPI()

# cors param
origins = [
    "https://test.dollarbillz.xyz",
    "https://dollarbillz.xyz",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# faucet endpoint
@app.get("/faucet/{address}")
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
