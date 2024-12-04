# wallet-creator
**Testnet only**
Create wallets on a specific shard of MultiversX and request testnet EGLD in one only command



## Installation
```
git clone https://github.com/VersaliXis/wallet-creator.git
python -m venv [/path to venv]
source [/path to venv]/bin/activate
pip install multiversx-sdk
```

## Use 
```
source [/path to venv]/bin/activate
python main.py
```

## Explanation
The script `main.py` creates 3 wallets on each of the three shards.  
It saves pem in `./wallets/`  
It then calls the API of the faucet `r3d4.fr` to get 1 EGLD on Testnet  

