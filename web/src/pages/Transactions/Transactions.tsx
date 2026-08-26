import type { Transaction } from "@/lib/generated";
import { searchTransactionsOptions } from "@/lib/generated/@tanstack/react-query.gen";
import TransactionsFilter from "./TransactionsFilter";
import { currencyColumn, dateColumn } from "@/utils/columnFormatters";
import useQueryForTable from "@/hooks/useQueryForTable";
import EntityTable from "@/components/EntityTable/EntityTable";
import EntityTableFilterAction from "@/components/EntityTable/EntityTableFilterAction";
import type { ColumnsType } from "antd/es/table";
import { useMemo } from "react";

export default function Transactions() {
  const columns = useMemo<ColumnsType<Transaction>>(
    () => [
      {
        title: "Date",
        dataIndex: "date",
        key: "date",
        ...dateColumn,
      },
      {
        title: "Amount",
        dataIndex: "amount",
        key: "amount",
        ...currencyColumn,
      },
      {
        title: "Summary",
        dataIndex: "summary",
        key: "summary",
        width: "30%",
      },
      {
        title: "Source",
        dataIndex: "transactionSourceName",
        key: "transactionSourceName",
      },
      {
        title: "Category",
        dataIndex: "transactionCategoryName",
        key: "transactionCategoryName",
      },
    ],
    [],
  );

  const { query, updateQuery, useQueryResult } = useQueryForTable(
    searchTransactionsOptions,
  );

  const filterAction = (
    <EntityTableFilterAction
      FilterForm={TransactionsFilter}
      query={query}
      updateQuery={updateQuery}
    />
  );

  return (
    <EntityTable
      title="Transactions"
      columns={columns}
      pagination={query}
      updatePagination={updateQuery}
      useQueryResult={useQueryResult}
      tableActions={[filterAction]}
    ></EntityTable>
  );
}
