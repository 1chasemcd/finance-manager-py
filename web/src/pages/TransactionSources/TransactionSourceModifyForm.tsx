import AppAutocomplete from "@/components/AppAutocomplete";
import type { WriteTransactionSource } from "@/lib/generated";
import { WriteTransactionSourceSchema } from "@/lib/generated/schemas.gen";
import { Form, Input } from "antd";

export default function TransactionSourceModifyForm() {
  return (
    <>
      <Form.Item<WriteTransactionSource>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input
          maxLength={WriteTransactionSourceSchema.properties.name.maxLength}
        />
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
