from typing import Protocol

from app.application.contract.repository_capabilities import (
    LookupHandler,
    SearchHandler,
)
from app.schemas.transaction import SearchTransactions, Transaction


class TransactionRepository(
    LookupHandler[Transaction], SearchHandler[Transaction, SearchTransactions], Protocol
):
    pass
