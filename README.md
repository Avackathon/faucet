# Funding Service

This [FastAPI](https://fastapi.tiangolo.com/) is a simple service that airdrops 10 $SUB token to a user's wallet in order to interact with the **SubNav Subnet** of the [SubNav](https://subnav.network) service.

## TL;DR

```
poetry install
poetry shell
./start.sh
```

**Note:** `files/account.pub` and `files/account.key` are intentionaly missing from the repo. These should contain the private and public key to the address used in the **subnav** evm instance genesis configuration file.

## Usage

To get 10 $SUB to use on the **SubNav Subnet**, simply PUT your wallet address to the `/faucet` endpoint.

```
curl https://api.subnav.network/faucet/0x70997970C51812dc3A010C7d01b50e0d17dc79C8
["0x263b8a1a25540216ec4fa3cfa7345f73939cd4cdfe1cd112924b0ba06b9786e3"]%
```

The command returns the transaction hash.
