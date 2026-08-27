from typing import Protocol

from app.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from app.schemas.import_def import ImportDef, WriteImportDef


class ImportDefRepository(
    LookupHandler[ImportDef],
    SearchHandler[ImportDef],
    CreateHandler[WriteImportDef],
    UpdateHandler[WriteImportDef],
    DeleteHandler,
    Protocol,
):
    pass
