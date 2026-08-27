import AppAutocomplete from "@/components/AppAutocomplete";
import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import type { WriteTransactionSource } from "@/lib/generated";
import {
  searchTransactionSourcesQueryKey,
  createTransactionSourceMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import { Form, Input } from "antd";

export default function TransactionSourceCreate() {
  return (
    <EntityCreateForm
      title="Add TransactionSource"
      createEntityMutation={createTransactionSourceMutation}
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
        <AppAutocomplete entity="person" />
      </Form.Item>
    </EntityCreateForm>
  );
}
