from typing import Protocol

from finance_manager.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from finance_manager.schemas.transaction_source import TransactionSource, WriteTransactionSource


class TransactionSourceRepository(
    LookupHandler[TransactionSource],
    SearchHandler[TransactionSource],
    CreateHandler[WriteTransactionSource],
    UpdateHandler[WriteTransactionSource],
    DeleteHandler,
    Protocol,
):
    pass
