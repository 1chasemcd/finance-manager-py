import AppAutocomplete from "@/components/AppAutocomplete";
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
import { Form, Input } from "antd";
import { useCallback } from "react";

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
      <Form.Item<WriteTransactionSource>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input maxLength={100} />
      </Form.Item>
      <Form.Item<WriteTransactionSource>
        label="Owner"
        name="ownerId"
        rules={[{ required: true }]}
      >
        <AppAutocomplete entityName="person" />
      </Form.Item>
    </EntityUpdateForm>
  );
}
