import {
  lookupTransactionCategoryOptions,
  searchTransactionCategoriesQueryKey,
  updateTransactionCategoryMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import TransactionCategoryModifyForm from "./TransactionCategoryModifyForm";
import EntityUpdateForm from "@/components/EntityForm/EntityUpdateForm";
import type { WriteTransactionCategory } from "@/lib/generated";

export default function TransactionCategoryUpdate() {
  return (
    <EntityUpdateForm
      title="Edit Category"
      lookupEntityOptions={lookupTransactionCategoryOptions}
      updateEntityMutation={updateTransactionCategoryMutation}
      dataTransform={(x) => x as WriteTransactionCategory}
      toInvalidate={[searchTransactionCategoriesQueryKey()]}
    >
      <TransactionCategoryModifyForm />
    </EntityUpdateForm>
  );
}
