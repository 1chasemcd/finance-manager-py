from pydantic import Field

from app.schemas.common import SchemaBase


class WriteImportDef(SchemaBase):
    name: str = Field(max_length=100)
    skip_rows: int = Field(default=0, ge=0, le=500)
    row_pattern: str | None = Field(default=None, max_length=500)

    date_index: int = Field(ge=0, le=500)
    summary_index: int = Field(ge=0, le=500)
    amount_index: int = Field(ge=0, le=500)

    date_format: str = Field(max_length=100)
    positive_is_spending: bool = False


class ImportDef(SchemaBase):
    id: int
    name: str
    skip_rows: int
    row_pattern: str

    date_index: int
    summary_index: int
    amount_index: int

    date_format: str
    positive_is_spending: bool
