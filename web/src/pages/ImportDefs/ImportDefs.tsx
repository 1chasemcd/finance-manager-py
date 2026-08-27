import EntityTable from "@/components/EntityTable/EntityTable";
import EntityTableCreateAction from "@/components/EntityTable/EntityTableCreateAction";
import useDeleteActionForTable from "@/hooks/useDeleteActionForTable";
import useEditActionForTable from "@/hooks/useEditActionForTable";
import useQueryForTable from "@/hooks/useQueryForTable";
import type { ImportDef } from "@/lib/generated";
import {
  deleteImportDefMutation,
  searchImportDefsOptions,
  searchImportDefsQueryKey,
} from "@/lib/generated/@tanstack/react-query.gen";
import type { ColumnsType } from "antd/es/table";
import { useMemo } from "react";

export default function ImportDefs() {
  const columns = useMemo<ColumnsType<ImportDef>>(
    () => [
      {
        title: "Name",
        dataIndex: "name",
        key: "name",
      },
    ],
    [],
  );
  const { query, updateQuery, useQueryResult } = useQueryForTable(
    searchImportDefsOptions,
  );

  const editAction = useEditActionForTable();
  const deleteAction = useDeleteActionForTable(deleteImportDefMutation, [
    searchImportDefsQueryKey(),
  ]);

  return (
    <EntityTable
      title="Import Definitions"
      columns={columns}
      pagination={query}
      updatePagination={updateQuery}
      useQueryResult={useQueryResult}
      tableActions={[<EntityTableCreateAction />]}
      rowActions={[editAction, deleteAction]}
    />
  );
}
