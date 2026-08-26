from typing import Protocol

from finance_manager.application.contract.repository_capabilities import (
    LookupHandler,
    SearchHandler,
)
from finance_manager.schemas.transaction import SearchTransactions, Transaction


class TransactionRepository(
    LookupHandler[Transaction], SearchHandler[Transaction, SearchTransactions], Protocol
):
    pass
