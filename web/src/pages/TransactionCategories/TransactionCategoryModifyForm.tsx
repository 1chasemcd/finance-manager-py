import type { WriteTransactionCategory } from "@/lib/generated";
import { Form, Input } from "antd";

export default function TransactionCategoryModifyForm() {
  return (
    <>
      <Form.Item<WriteTransactionCategory>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input maxLength={100} />
      </Form.Item>
      <Form.Item<WriteTransactionCategory>
        label="Description"
        name="description"
      >
        <Input maxLength={500} />
      </Form.Item>
    </>
  );
}
