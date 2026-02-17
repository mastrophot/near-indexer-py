from pydantic import BaseModel, Field
from typing import List, Optional, Any

class TransactionModel(BaseModel):
    transaction_hash: str
    signer_id: str
    receiver_id: str
    block_hash: str
    block_timestamp: Optional[int] = None
    actions: List[Any] = Field(default_factory=list)
    status: Optional[str] = None

class ReceiptModel(BaseModel):
    receipt_id: str
    predecessor_id: str
    receiver_id: str
    receipt: dict

class OutcomeModel(BaseModel):
    id: str
    outcome: dict
    proof: List[dict]
    block_hash: str

class BlockModel(BaseModel):
    author: str
    header: dict
    chunks: List[dict]

class IndexerStats(BaseModel):
    total_transactions: int
    last_block_height: int
    active_accounts: int
