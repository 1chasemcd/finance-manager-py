import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import {
  searchCategoryPatternsQueryKey,
  createCategoryPatternMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import CategoryPatternModifyShared from "./CategoryPatternModifyShared";
import { Form } from "antd";
import type { WriteCategoryPattern } from "@/lib/generated";

export default function CategoryPatternCreate() {
  const [form] = Form.useForm<WriteCategoryPattern>();
  return (
    <EntityCreateForm
      title="Add Category Pattern"
      createEntityMutation={createCategoryPatternMutation}
      toInvalidate={[searchCategoryPatternsQueryKey()]}
      form={form}
    >
      <CategoryPatternModifyShared form={form} />
    </EntityCreateForm>
  );
}
