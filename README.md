# Funding Service

## TL;DR

```
poetry install
poetry shell
uvicorn main:app --reload
```

## Usage

To get 10 $SUB to use on the subnet, simply PUT your wallet address to the `/fauce` endpoint.

```
curl -X PUT http://127.0.0.1:8000/faucet/0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
["0x263b8a1a25540216ec4fa3cfa7345f73939cd4cdfe1cd112924b0ba06b9786e3"]%
```

The command returns the transaction hash.
