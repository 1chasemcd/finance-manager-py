import EntityUpdateForm from "@/components/EntityForm/EntityUpdateForm";
import type {
  TransactionSource,
  WriteTransactionSource,
} from "@/lib/generated";
import {
  lookupTransactionSourceOptions,
  searchTransactionSourcesQueryKey,
  updateTransactionSourceMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import { useCallback } from "react";
import TransactionSourceModifyForm from "./TransactionSourceModifyForm";

export default function TransactionSourceUpdate() {
  const dataTransform = useCallback(
    (data: TransactionSource) => data as WriteTransactionSource,
    [],
  );
  return (
    <EntityUpdateForm
      title="Edit Transaction Source"
      lookupEntityOptions={lookupTransactionSourceOptions}
      updateEntityMutation={updateTransactionSourceMutation}
      dataTransform={dataTransform}
      toInvalidate={[searchTransactionSourcesQueryKey()]}
    >
      <TransactionSourceModifyForm />
    </EntityUpdateForm>
  );
}
