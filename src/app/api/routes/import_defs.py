from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from app.api.result_handler import handle_result, handled_error_responses
from app.dependencies.import_defs import ImportDefRepositoryDep
from app.schemas.common import PagedQuery, SearchResponse
from app.schemas.import_def import ImportDef, WriteImportDef

router = APIRouter(prefix="/importdefs")


@router.get(
    "/{id}",
    response_model=ImportDef,
    responses=handled_error_responses(),
)
async def lookup_import_def(
    id: int,
    repo: ImportDefRepositoryDep,
) -> ImportDef | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.get(
    "/",
    response_model=SearchResponse[ImportDef],
    responses=handled_error_responses(),
)
async def search_import_defs(
    request: Annotated[PagedQuery, Query()],
    repo: ImportDefRepositoryDep,
) -> SearchResponse[ImportDef] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_import_def(
    request: WriteImportDef,
    repo: ImportDefRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_import_def(
    id: int,
    request: WriteImportDef,
    repo: ImportDefRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_import_def(
    id: int,
    repo: ImportDefRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
