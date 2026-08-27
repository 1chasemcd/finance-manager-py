import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import {
  searchTransactionSourcesQueryKey,
  createTransactionSourceMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import TransactionSourceModifyForm from "./TransactionSourceModifyForm";

export default function TransactionSourceCreate() {
  return (
    <EntityCreateForm
      title="Add Transaction Source"
      createEntityMutation={createTransactionSourceMutation}
      toInvalidate={[searchTransactionSourcesQueryKey()]}
    >
      <TransactionSourceModifyForm />
    </EntityCreateForm>
  );
}
