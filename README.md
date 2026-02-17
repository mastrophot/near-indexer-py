# near-indexer-py

Python utilities for building NEAR Protocol indexing pipelines.

## Features

- **Pydantic Models:** Robust type-safe models for Blocks, Transactions, Receipts, and Outcomes.
- **RPC Client:** Simplified interface to interact with NEAR RPC with built-in retry logic.
- **Indexing Helpers:** Structured for integration with data warehouses or real-time pipelines.

## Installation

```bash
pip install near-indexer-py
```

## Usage

### Using Models

```python
from near_indexer.models import TransactionModel

data = {
    "hash": "...",
    "signer_id": "bob.near",
    "receiver_id": "alice.near",
    "block_hash": "...",
    "block_timestamp": 123456789,
    "actions": []
}
tx = TransactionModel(**data)
print(tx.signer_id)
```

### Using the RPC Client

```python
from near_indexer.client import NearRpcClient

client = NearRpcClient("https://rpc.mainnet.near.org")
block = client.get_block(height=123456)
print(block)
```

## License

MIT
