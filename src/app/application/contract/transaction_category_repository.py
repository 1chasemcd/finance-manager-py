from typing import Protocol

from app.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from app.schemas.transaction_category import (
    TransactionCategory,
    WriteTransactionCategory,
)


class TransactionCategoryRepository(
    LookupHandler[TransactionCategory],
    SearchHandler[TransactionCategory],
    CreateHandler[WriteTransactionCategory],
    UpdateHandler[WriteTransactionCategory],
    DeleteHandler,
    Protocol,
):
    pass
