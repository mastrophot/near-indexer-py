import requests
import time
from typing import List, Optional, Dict, Any
from .models import TransactionModel, BlockModel

class NEARIndexerClient:
    def __init__(self, rpc_url: str = "https://rpc.mainnet.near.org"):
        self.rpc_url = rpc_url

    def _post(self, method: str, params: Any) -> Dict:
        payload = {
            "jsonrpc": "2.0",
            "id": "near-indexer-py",
            "method": method,
            "params": params
        }
        for _ in range(3):  # Simple retry logic
            try:
                response = requests.post(self.rpc_url, json=payload, timeout=10)
                response.raise_for_status()
                return response.json().get("result", {})
            except Exception:
                time.sleep(1)
        raise Exception(f"Failed to call {method} after 3 retries")

    def get_block(self, block_id: Any) -> BlockModel:
        result = self._post("block", {"block_id": block_id})
        return BlockModel(**result)

    def get_transaction(self, tx_hash: str, account_id: str) -> TransactionModel:
        result = self._post("tx", [tx_hash, account_id])
        return TransactionModel(**result)

    def list_transactions_for_account(self, account_id: str, limit: int = 10) -> List[TransactionModel]:
        # This typically requires an archival node or a specific indexer API
        # Here we mock the pagination/filtering logic for the exercise
        print(f"Mocking transaction list for {account_id} with limit {limit}")
        return []
