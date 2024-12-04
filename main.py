from pathlib import Path
from multiversx_sdk import Mnemonic, Address, UserPEM
from multiversx_sdk.core.address import get_shard_of_pubkey
from use_faucet import request_testnet_EGLD

PATH = Path("./wallets")
NUMBER_OF_SHARDS = 3
AVAILABLE_SHARDS = [0,1,2]
MAX_ITERATIONS = 100

class ExceededMaxLoopIterationException(Exception):
    "Raised when the loop exceeds maximum iteration"
    pass

#Generate 3 wallets in each of the shards
def generate_and_fill_wallets():
    for shard_id in AVAILABLE_SHARDS:
        for i in range(3):
            address, mnemonic = new_mnemonic_in_shard(i, shard_id)
            print(f"\n\nGenerated {address} in shard {shard_id}")
            request_testnet_EGLD(address)

#Create a new mnemonic in a given shard
def new_mnemonic_in_shard(wallet_id: int, shard_index: int) -> (str, Mnemonic):
    for _ in range(MAX_ITERATIONS):
        mnemonic = Mnemonic.generate()
        secret_key = mnemonic.derive_key(0)
        pubkey = mnemonic.derive_key().generate_public_key()
        generated_address_shard = get_shard_of_pubkey(pubkey.buffer, NUMBER_OF_SHARDS)

        if shard_index == generated_address_shard:
            address = Address(pubkey.buffer, "erd").to_bech32()
            pem = UserPEM(label = address, secret_key=secret_key)
            pem.save(PATH / f"wallet_{wallet_id}_shard_{shard_index}.pem")
            return address, mnemonic

    raise ExceededMaxLoopIterationException

if __name__ == "__main__":
    print("Generating and requesting faucet for three new wallets on shard 0, 1 and 2 on Testnet")
    generate_and_fill_wallets()
