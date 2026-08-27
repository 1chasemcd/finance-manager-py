import type { WriteTransactionCategory } from "@/lib/generated";
import { WriteTransactionCategorySchema } from "@/lib/generated/schemas.gen";
import { Form, Input } from "antd";

export default function TransactionCategoryModifyForm() {
  return (
    <>
      <Form.Item<WriteTransactionCategory>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input
          maxLength={WriteTransactionCategorySchema.properties.name.maxLength}
        />
      </Form.Item>
      <Form.Item<WriteTransactionCategory>
        label="Description"
        name="description"
      >
        <Input
          maxLength={
            WriteTransactionCategorySchema.properties.description.anyOf[0]
              .maxLength
          }
        />
      </Form.Item>
    </>
  );
}
