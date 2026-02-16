import pytest
from near_indexer.client import NEARIndexerClient
from near_indexer.models import TransactionModel

def test_client_init():
    client = NEARIndexerClient()
    assert client.rpc_url == "https://rpc.mainnet.near.org"

def test_model_validation():
    data = {
        "hash": "abc",
        "signer_id": "alice.near",
        "receiver_id": "bob.near",
        "block_hash": "xyz",
        "block_timestamp": 123456789,
        "actions": []
    }
    tx = TransactionModel(**data)
    assert tx.signer_id == "alice.near"
    assert tx.block_timestamp == 123456789
