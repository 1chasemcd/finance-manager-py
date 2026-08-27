import type { WriteImportDef } from "@/lib/generated";
import { Form, Input } from "antd";

export default function ImportDefModifyForm() {
  return (
    <>
      <Form.Item<WriteImportDef>
        label="Name"
        name="name"
        rules={[{ required: true }]}
      >
        <Input maxLength={100} />
      </Form.Item>
    </>
  );
}
