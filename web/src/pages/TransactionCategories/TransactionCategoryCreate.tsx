import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import {
  searchTransactionCategoriesQueryKey,
  createTransactionCategoryMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import TransactionCategoryModifyForm from "./TransactionCategoryModifyForm";

export default function TransactionCategoryCreate() {
  return (
    <EntityCreateForm
      title="Add Category"
      createEntityMutation={createTransactionCategoryMutation}
      toInvalidate={[searchTransactionCategoriesQueryKey()]}
    >
      <TransactionCategoryModifyForm />
    </EntityCreateForm>
  );
}
