import type { WritePerson } from "@/lib/generated";
import { WritePersonSchema } from "@/lib/generated/schemas.gen";
import { Form, Input } from "antd";

export default function PersonModifyForm() {
  return (
    <>
      <Form.Item<WritePerson>
        label="First Name"
        name="firstName"
        rules={[{ required: true }]}
      >
        <Input maxLength={WritePersonSchema.properties.firstName.maxLength} />
      </Form.Item>
      <Form.Item<WritePerson>
        label="Last Name"
        name="lastName"
        rules={[{ required: true }]}
      >
        <Input maxLength={WritePersonSchema.properties.lastName.maxLength} />
      </Form.Item>
    </>
  );
}
