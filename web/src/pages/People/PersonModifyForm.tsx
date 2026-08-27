import type { WritePerson } from "@/lib/generated";
import { Form, Input } from "antd";

export default function PersonModifyForm() {
  return (
    <>
      <Form.Item<WritePerson>
        label="First Name"
        name="firstName"
        rules={[{ required: true }]}
      >
        <Input maxLength={100} />
      </Form.Item>
      <Form.Item<WritePerson>
        label="Last Name"
        name="lastName"
        rules={[{ required: true }]}
      >
        <Input maxLength={100} />
      </Form.Item>
    </>
  );
}
