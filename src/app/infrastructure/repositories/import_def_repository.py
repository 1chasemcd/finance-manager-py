from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.import_def_row import ImportDefRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.import_def import ImportDef, WriteImportDef


class ImportDefRepositoryImpl(BaseRepository[ImportDefRow, ImportDef, WriteImportDef]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(ImportDefRow, ImportDef, session)
