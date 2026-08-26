import {
  lookupCategoryPatternOptions,
  searchCategoryPatternsQueryKey,
  updateCategoryPatternMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import CategoryPatternModifyShared from "./CategoryPatternModifyShared";
import EntityUpdateForm from "@/components/EntityForm/EntityUpdateForm";
import type { WriteCategoryPattern } from "@/lib/generated";
import { Form } from "antd";

export default function CategoryPatternUpdate() {
  const [form] = Form.useForm<WriteCategoryPattern>();

  return (
    <EntityUpdateForm
      title="Edit Category Pattern"
      lookupEntityOptions={lookupCategoryPatternOptions}
      updateEntityMutation={updateCategoryPatternMutation}
      dataTransform={(x) => x as WriteCategoryPattern}
      toInvalidate={[searchCategoryPatternsQueryKey()]}
      form={form}
    >
      <CategoryPatternModifyShared form={form} />
    </EntityUpdateForm>
  );
}
