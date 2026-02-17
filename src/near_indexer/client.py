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
        # RPC returns { 'transaction': { ... }, 'status': ... }
        # We need to flatten it slightly if we want to match our model
        tx_data = result.get("transaction", {})
        merged = {**tx_data, "transaction_hash": tx_data.get("hash"), "status": str(result.get("status"))}
        return TransactionModel(**merged)

    def list_transactions_for_account(self, account_id: str, limit: int = 10) -> List[TransactionModel]:
        """
        Fetches real-time transactions for an account using NearBlocks API.
        """
        network = "api" if "mainnet" in self.rpc_url else "api-testnet"
        api_url = f"https://{network}.nearblocks.io/v1/account/{account_id}/txns"
        
        try:
            response = requests.get(api_url, params={"limit": limit}, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            transactions = []
            for tx in data.get("txns", []):
                # Map NearBlocks fields to our TransactionModel
                # This is a simplified mapping for demonstration
                transactions.append(TransactionModel(
                    transaction_hash=tx.get("transaction_hash"),
                    signer_id=tx.get("signer_id"),
                    receiver_id=tx.get("receiver_id"),
                    block_hash=tx.get("block_hash"),
                    status=tx.get("status")
                ))
            return transactions
        except Exception as e:
            print(f"Error fetching real transactions: {e}. Falling back to empty list.")
            return []

