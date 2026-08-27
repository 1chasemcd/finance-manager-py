import AppAutocomplete from "@/components/AppAutocomplete";
import type { WriteTransactionSource } from "@/lib/generated";
import { Form, Input } from "antd";

export default function TransactionSourceModifyForm() {
  return (
    <>
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
    </>
  );
}
