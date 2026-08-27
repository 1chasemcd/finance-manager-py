import type { WriteImportDef } from "@/lib/generated";
import { WriteImportDefSchema } from "@/lib/generated/schemas.gen";
import { Form, Input } from "antd";

export default function ImportDefModifyForm() {
  return (
    <>
      <Form.Item<WriteImportDef>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input maxLength={WriteImportDefSchema.properties.name.maxLength} />
      </Form.Item>
    </>
  );
}
