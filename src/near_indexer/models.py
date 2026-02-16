from pydantic import BaseModel, Field
from typing import List, Optional, Any

class TransactionModel(BaseModel):
    hash: str
    signer_id: str = Field(..., alias="signer_id")
    receiver_id: str = Field(..., alias="receiver_id")
    block_hash: str
    block_timestamp: int
    actions: List[Any]

class BlockModel(BaseModel):
    author: str
    header: dict
    chunks: List[dict]

class IndexerStats(BaseModel):
    total_transactions: int
    last_block_height: int
    active_accounts: int
