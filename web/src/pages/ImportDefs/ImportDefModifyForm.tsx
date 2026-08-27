import type { WriteImportDef } from "@/lib/generated";
import { WriteImportDefSchema } from "@/lib/generated/schemas.gen";
import { Checkbox, Divider, Flex, Form, Input, InputNumber } from "antd";

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
      <Flex gap="small">
        <Form.Item<WriteImportDef>
          label="Rows To Skip"
          name="skipRows"
          rules={[{ required: true }]}
          style={{ margin: 0 }}
        >
          <InputNumber
            defaultValue={0}
            max={WriteImportDefSchema.properties.skipRows.maximum}
            min={WriteImportDefSchema.properties.skipRows.minimum}
          />
        </Form.Item>

        <Form.Item<WriteImportDef>
          label="Row Pattern"
          name="rowPattern"
          style={{ flex: 1, margin: 0 }}
        >
          <Input
            style={{ fontFamily: "monospace" }}
            maxLength={
              WriteImportDefSchema.properties.rowPattern.anyOf[0].maxLength
            }
          />
        </Form.Item>
      </Flex>
      <Divider />
      <Flex gap="large">
        <div>
          <Form.Item<WriteImportDef>
            label="Amount Column"
            name="amountIndex"
            rules={[{ required: true }]}
          >
            <InputNumber
              max={WriteImportDefSchema.properties.amountIndex.maximum}
              min={WriteImportDefSchema.properties.amountIndex.minimum}
            />
          </Form.Item>
          <Form.Item<WriteImportDef>
            label="Date Column"
            name="dateIndex"
            rules={[{ required: true }]}
          >
            <InputNumber
              max={WriteImportDefSchema.properties.dateIndex.maximum}
              min={WriteImportDefSchema.properties.dateIndex.minimum}
            />
          </Form.Item>
          <Form.Item<WriteImportDef>
            label="Summary Column"
            name="summaryIndex"
            rules={[{ required: true }]}
          >
            <InputNumber
              max={WriteImportDefSchema.properties.summaryIndex.maximum}
              min={WriteImportDefSchema.properties.summaryIndex.minimum}
            />
          </Form.Item>
        </div>

        <div style={{ flex: 1 }}>
          <Form.Item<WriteImportDef>
            name="positiveIsSpending"
            rules={[{ required: true }]}
          >
            <Checkbox>Spending is positive amount</Checkbox>
          </Form.Item>
          <Form.Item<WriteImportDef>
            name="dateFormat"
            rules={[{ required: true, message: "Date Format is required" }]}
          >
            <Input
              placeholder="Specify date format"
              style={{ fontFamily: "monospace" }}
              maxLength={WriteImportDefSchema.properties.dateFormat.maxLength}
            />
          </Form.Item>
        </div>
      </Flex>
    </>
  );
}
