import AppAutocomplete from "@/components/AppAutocomplete";
import AppDatePicker, {
  dateConverterProps,
} from "@/components/AppDatePicker.tsx";
import type { SearchTransactionsData } from "@/lib/generated";
import { Flex, Form, type FormInstance } from "antd";
import InputCurrency from "@/components/InputCurrency";

type TransactionQuery = NonNullable<SearchTransactionsData["query"]>;

type TransactionsFilterPageProps = {
  form: FormInstance<TransactionQuery>;
};

export default function TransactionsFilter({
  form,
}: TransactionsFilterPageProps) {
  return (
    <Form<TransactionQuery> form={form} layout="vertical">
      <Form.Item label="Date Range">
        <Flex gap="small">
          <Form.Item<TransactionQuery>
            {...dateConverterProps}
            name="minDate"
            noStyle
            style={{ flex: 1 }}
          >
            <AppDatePicker placeholder="From" style={{ width: "100%" }} />
          </Form.Item>
          <Form.Item<TransactionQuery>
            {...dateConverterProps}
            name="maxDate"
            noStyle
            style={{ flex: 1 }}
          >
            <AppDatePicker placeholder="To" style={{ width: "100%" }} />
          </Form.Item>
        </Flex>
      </Form.Item>

      <Form.Item label="Amount Range">
        <Flex gap="small">
          <Form.Item<TransactionQuery>
            name="minAmount"
            noStyle
            style={{ flex: 1 }}
          >
            <InputCurrency placeholder="Low" />
          </Form.Item>
          <Form.Item<TransactionQuery>
            name="maxAmount"
            noStyle
            style={{ flex: 1 }}
          >
            <InputCurrency placeholder="High" />
          </Form.Item>
        </Flex>
      </Form.Item>

      <Form.Item<TransactionQuery> label="Source" name="transactionSourceId">
        <AppAutocomplete entityName="transactionsource" />
      </Form.Item>

      <Form.Item<TransactionQuery>
        label="Category"
        name="transactionCategoryId"
      >
        <AppAutocomplete entityName="transactioncategory" />
      </Form.Item>

      <Form.Item<TransactionQuery> label="Owner" name="ownerId">
        <AppAutocomplete entityName="person" />
      </Form.Item>
    </Form>
  );
}
