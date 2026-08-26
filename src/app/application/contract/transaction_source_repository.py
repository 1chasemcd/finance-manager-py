from typing import Protocol

from app.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from app.schemas.transaction_source import TransactionSource, WriteTransactionSource


class TransactionSourceRepository(
    LookupHandler[TransactionSource],
    SearchHandler[TransactionSource],
    CreateHandler[WriteTransactionSource],
    UpdateHandler[WriteTransactionSource],
    DeleteHandler,
    Protocol,
):
    pass
