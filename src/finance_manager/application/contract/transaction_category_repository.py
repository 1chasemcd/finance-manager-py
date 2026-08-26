from typing import Protocol

from finance_manager.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from finance_manager.schemas.transaction_category import (
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
